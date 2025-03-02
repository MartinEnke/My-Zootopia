import html
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
    #print(f"Name: {name}\nDiet: {diet}\nLocation: {location}")

    #if "type" in animal["characteristics"]:
        #print(f"Type: {animal["characteristics"]["type"]}")

    #print()

def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]} <br/>"
    output += f"<strong>Location:</strong> {", ".join(animal["locations"])} <br/>\n"
    if "color" in animal["characteristics"]:
        output += f"<strong>Color:</strong> {animal["characteristics"]["color"]} <br/>\n"
    if "prey" in animal["characteristics"]:
        output += f"<strong>Prey:</strong> {animal["characteristics"]["prey"]} <br/>\n"
    if "main_prey" in animal["characteristics"]:
        output += f"<strong>Main Prey:</strong> {animal["characteristics"]["main_prey"]} <br/>\n"
    if "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal["characteristics"]["type"]} <br/>\n"
    if "scientific_name" in animal["taxonomy"]:
        output += f"<strong>Scientific Name:</strong> {animal["taxonomy"]["scientific_name"]} <br/>\n"
    output += "</p>"
    output += "</li>"
    return output


output = ''
for animal in animals_data:
    output += serialize_animal(animal)


#export
text = "__REPLACE_ANIMALS_INFO__"
text_update = text.replace(text, output)

with open("animals_template.html", "r") as file:
    html_content = file.read()

update_content = html_content.replace(text, text_update)

with open("animals_template.html", "w", encoding="utf-8") as file:
    file.write(update_content)


print("HTML file updated successfully!")













