import json
intent = []
response = []
with open('./story/rasa_story.md', 'r') as stories:
    for line in stories.readlines():
        if '*' in line:
            if line.replace("*",'').replace(' ','').replace('\n','') not in intent:
                intent.append(line.replace("*",'').replace(' ','').replace('\n','').replace("(",'').replace(")",''))
        elif '-' in line and '##' not in line:
            check = line.replace(' ','').replace('\n','')[1:]
            if check not in response:
                response.append(check.replace("(",'').replace(")",''))

new_intent = []
new_response = []
for i in intent:
    if i != '':
        new_intent.append('  - %s' % i)

for r in response:
    if r != '' or r != '\n ':
        new_response.append('  - %s' % r)

with open('./domain/domain.yml','a') as result:
    result.writelines("intents:\n")
    result.writelines('\n'.join(new_intent))
    result.writelines('\n')
    result.writelines("actions:\n")
    result.writelines('\n'.join(new_response))
    result.writelines('\n')
    with open('./response/en/rasa_response.json') as source:
        result.writelines("templates:\n")
        json_source = json.load(source)
        for resp in json_source:
            for r in json_source[resp]:
                if 'utter_' in r['name']:
                    result.writelines('  '+r['name']+':\n')
                    result.writelines('  - "'+r['payload'].replace('"',"'")+'"\n')



