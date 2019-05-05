import json, re




def generate_text(generated_id, name):
    return generated_id, "utter_%s" % name

def generate_custom(generated_id, name):
    return generated_id, "action_%s" % name

def generate_quickreplies(text, elements):
    el = []
    for element in elements:
        el.append({
            "title": element['title'],
            "payload": '/%s' % element['link'].lower().replace("-"," ").replace("/"," ").replace(" ","_")
        })

    return {
            "type": "quickreplies",
            "elements" : [{
                "text": text,
                "replies":el
            }]
        }

def make_payload(rasa_action, payload):
    rasa_action = rasa_action.lower().replace("-"," ").replace("/"," ").replace(" ","_").replace("(",'').replace(")",'')
    rasa_action = re.sub(r'___','_',rasa_action)
    rasa_action = re.sub(r'__','_',rasa_action)
    return {
        "name": rasa_action,
        "payload": payload
    }

def make_carousel(elements):
    el = []
    for element in elements:
        btns = element['buttons']
        btn = []
        for bt in btns:
            btn.append({
                "title":bt['title'],
                "payload":'/%s' % bt['link'].lower().replace("-"," ").replace("/"," ").replace(" ","_")
            })
        el.append({
                    "label":element['title'],
                    "description":element['subtitle'],
                    "image_type":"url",
                    "image":element['image_url'],
                    "buttons":btn
                })
    return {
        "type": "carousel",
        "elements" : el
    }

def make_list(elements):
    el = []
    for element in elements:
        btn = []
        for button in element['buttons']:
            btn_component = {
                "title": button['title'],
                "payload": button['link']
            }
            btn.append(btn_component)
        list_component = {
            "image" :element['imageUrl'],
            "image_type": "url",
            "label": element['title'],
            "description": element['subtitle'],
            "buttons": btn
        }
        el.append(list_component)
    
    list_result = {
        "type": "list",
        "text": "list",
        "data": el
    }
    return list_result


        


def by_type(R, res_type):
    content_value = None
    if res_type == "text":
        content_value = {
            "content":{
                "type": "texts",
                "elements":[
                    R['content']
                ]
            }
        }
    elif res_type == "buttons":
        buttons = R['content']['elements']
        replies = []
        for button in buttons:
            replies.append({
                "title": button['title'],
                "payload": button['link'] if isURL(button['link']) else "/"+button['link'].replace(" ","_").lower()
            })
        content_value = {
            "content":{
                "type": "quickreplies",
                "elements":[
                    {
                        "text": R['content']['text'],
                        "replies": replies
                    }
                ]
            }
        }
    elif res_type == "generic":
        content_value ={
           "content" : make_carousel(R['content']['elements'])
        } 
    elif res_type == "list":
        content_value = {
            "content":make_list(R['content']['elements'])
        }
    elif res_type == "form":
        content_value = {
            "content" : {
                "type": "form",
                "elements": [R['content']['json']]
            }
        }
    elif res_type == "webhook":
        content_value = {
            "content" : {
                "type": "webhook",
                "elements": [R['content']]
            }
        }
    else:
        content_value = {
            "content" : {
                "type": res_type,
                "elements": [R['content']]
            }
        }

    return content_value


def isURL(url):
    fURL = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    if len(fURL) > 0:
        return True
    else:
        return False