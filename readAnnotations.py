import os
import json

dataset_path = os.path.join(os.path.expanduser("~"), "Desktop/LNN/TACO Stuff/data")
anns_file_path = dataset_path + '/annotations.json'


# Open the JSON file
with open(anns_file_path, 'r') as file:
    # Read the JSON content
    json_content = file.read()

    # Parse the JSON content
    data = json.loads(json_content)

    # Now 'data' contains the JSON content as a Python data structure (usually a dictionary)
    print(data)
    print("\n")
    print(len(data))
    print("\n")
    for key in data.keys():
        print(key)
