import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents as a list of dictionaries.
    """
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data