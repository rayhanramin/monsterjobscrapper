import json

with open('issue_list.json') as json_data:
    data = json.load(json_data)
    for element in data:
        print(element['Bug_id'])