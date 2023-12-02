import json
intents = open('/kaggle/input/unity3d-faq/intents.json','r').readlines()
dataframe = []
for intent in intents:
    intents_json = json.loads(intent)
    for sent in intents_json['intents']:
        dataframe.append({
            'id':intents_json['id'],
            'user_id': intents_json['user_id'],
            'tags': intents_json['tags'],
            'question': sent,
            'answer': intents_json['answer']
        })
#     dataframe.append(intents_json)
df = pd.DataFrame(dataframe)
df.to_csv('gamedev.csv',index=None)
