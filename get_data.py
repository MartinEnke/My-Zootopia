import json

def get_animal_data(file_path):
    """Load animals data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
