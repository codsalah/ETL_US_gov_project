import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents as a list of dictionaries.
    """
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"JSON decoding error in file {file_path}: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
    return data