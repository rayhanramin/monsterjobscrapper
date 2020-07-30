import csv
import json

# create a dictionary
data = {}

# Open a csv reader called DictReader
with open('bugfixing_commits_git_hub_firefox.csv', 'r') as csvf:
    csvReader = list(csv.DictReader(csvf))

    # Convert each row into a dictionary
    # and add it to data
    for rows in csvReader:
        # Assuming a column named 'No' to
        # be the primary key
        key = rows['Bug_id']
        del rows['Bug_id']
        data[key] = rows


# Open a json writer, and use the json.dumps()
# function to dump data
with open('issue_list.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))