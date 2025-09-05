import json

def read_json_file(file_path):
    """Reads a JSON file and returns its content as a Python dictionary."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    # Example usage
    file_path = 'Database/dataset.json'
    data = read_json_file(file_path)
    for i in data:
        print(data[i][0]["name"])