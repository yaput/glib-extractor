import json

def make_common_example(text="", intent_name=""):
    return {
        'text': text,
        'intent': intent_name,
        'entities':[]
    }
def extractor(lang="en", intent_json=None, project=""):
    if intent_json != None:
        intent_name = intent_json['title'].lower().replace(' ','_')
        examples = []
        if lang in intent_json['data'].keys():
            for example in intent_json['data'][lang]:
                examples.append(make_common_example(example['content'],intent_name))

    with open('./intents/%s/%s/rasa_intent_%s_%s.json' % (project,lang,intent_name,lang), 'a') as rasa_intent:
        rasa_intent_format = {
            'rasa_nlu_data':{
                'common_examples':examples,
                'entity_synonyms':[]
            }
        }
        rasa_intent.write(json.dumps(rasa_intent_format,indent=3, ensure_ascii=False))

# with open('./source/intents.json') as source:
#     source_json = json.load(source)
#     for src in source_json:
#         intent_src = source_json[src]
#         extractor(lang='en', intent_json=intent_src)
#         extractor(lang='ar', intent_json=intent_src)