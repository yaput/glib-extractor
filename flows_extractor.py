import json
actions = None
with open('./response/en/rasa_response.json') as resp:
    actions = json.load(resp)
    
def write_story(generate_id, inputs, responses):
    temp_input = []
    temp_response = []
    for input in inputs:
        write_input = input['content']
        if 'type' in input.keys():
            if input['type'] == 'Intent' or input['type'] == 'intent':
                write_input = input['title']
            elif input['type'] == 'Entity':
                continue
        temp_input.append(write_input.lower().replace(' ', '_').replace("(",'').replace(")",''))
    for response in responses:
        write_action = response['content']
        if response['content'] in actions.keys():
            write_action = actions[response['content']]
            for act in write_action:
                if act != None and act['name']:
                    temp_response.append("  - %s" % act['name'].replace("(",'').replace(")",''))
        else:
            temp_response.append("  - %s" % write_action)
    with open('./story/rasa_story.md', 'a') as rasa_story:
        rasa_story.write("## story %s\n" % generate_id)
        rasa_story.write("* %s\n" % (' OR '.join(temp_input)))
        rasa_story.write('\n'.join(temp_response))
        rasa_story.write("\n\n")

with open('./source/flows.json') as flow:
    flow_json = json.load(flow)
    for id in flow_json:
        flow_raw = flow_json[id]
        write_story(flow_raw['title'].lower().replace(' ','_'), flow_raw['data']['inputs'], flow_raw['data']['responses'])