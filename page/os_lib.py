import json

def read_json_file(filepath: str):
    '''Read and return the JSON content of the file.'''
    with open(filepath, 'r', encoding='UTF-8') as file:
        return json.load(file)
