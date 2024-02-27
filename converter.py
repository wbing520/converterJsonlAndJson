import json
import os

# try this code to get the real path
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

# # Convert JSON to JSONL
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)
#     with open('data.jsonl', 'w') as jsonl_file:
#         for item in data:
#             jsonl_file.write(json.dumps(item) + '\n')

# Convert JSONL to JSON
with open('./data_clean/jsonlTojson/US_qbank.jsonl', encoding='utf-8') as jsonl_file:
    data = []
    for line in jsonl_file:
        data.append(json.loads(line))
    with open('./data_clean/jsonlTojson/US_qbank.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

