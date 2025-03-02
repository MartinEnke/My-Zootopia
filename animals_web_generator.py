import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file:
        return json.load(file)

animals_data = load_data('animals_data.json')

print(animals_data)


for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = ", ".join(animal["locations"])
    print(f"Name: {name}\nDiet: {diet}\nLocation: {location}")

    if "type" in animal["characteristics"]:
        print(f"Type: {animal["characteristics"]["type"]}")

    print()






