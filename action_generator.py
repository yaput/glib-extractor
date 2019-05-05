import json

with open('./response/en/rasa_response.json') as responses:
    responses_json = json.load(responses)
    with open('./action/action.py', 'a') as action_py:
        action_py.writelines('from rasa_core_sdk import Action\n')
        action_py.writelines('from cache_client import cache\n')
        action_py.writelines('from rasa_core_sdk.events import Restarted\n')
        for gen_id in responses_json:
            for resp in responses_json[gen_id]:
                if 'utter' not in resp['name']:
                    class_name = resp['name'].split('_')
                    new_name = ""
                    for name in class_name:
                        new_name+=name[0].upper()+name[1:]
                    
                    pyld = resp['payload']
                    if 'http' in pyld:
                        pyld = '"'+pyld+'"'
                    action_py.writelines('class %s(Action):\n' % new_name.replace("&",'').replace("(",'').replace(")",''))
                    action_py.writelines('    def name(self):\n')
                    action_py.writelines('        return "%s"\n' % resp['name'])
                    action_py.writelines('    def run(self, dispatcher, tracker, domain):\n')
                    action_py.writelines('        payload = %s\n' % pyld)
                    action_py.writelines('        dispatcher.utter_attachment(payload)\n')
                    action_py.writelines('        return\n\n')
                