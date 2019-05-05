import json
from intent_extractor import extractor
from response_extractor import by_type

with open("./Avivo.json") as f:
    nb = json.load(f)
    # FOR RASA INTENT
    # intents = nb["intents"]
    # for intent in intents:
    #     extractor(lang='ar',intent_json=intents[intent], project="national_bonds")
    responses = nb["responses"]
    full = {}
    for response in responses:
        name = responses[response]['title'].lower().replace("-"," ").replace("/"," ").replace(" ","_")
        count = 0
        for i in range(len(responses[response]['data']['en'][0])):
            content = {}
            key_name = "utter_"+name
            if count > 0:
                key_name = key_name + "_" + str(count)
            content['en'] = by_type(responses[response]['data']['en'][0][i],responses[response]['data']['en'][0][i]['type'])
            try:
                content['ar'] = by_type(responses[response]['data']['ar'][0][i],responses[response]['data']['en'][0][i]['type'])
            except:
                pass
            full[key_name] = content
            # print("====")
            # print(key_name)
            # print(content)
            count += 1

    print(full)

    with open('./response/avivo/response.json', 'a') as w:
        w.write(json.dumps(full,indent=3,ensure_ascii=False))