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


output = ""  # define an empty string
for animal in animals_data:
    # append information to each string
    output += f"Name: {animal["name"]}\n"
    output += f"Diet: {animal["characteristics"]["diet"]}\n"
    output += f"Location: {", ".join(animal["locations"])}\n"
    if "type" in animal["characteristics"]:
        output += f"Type: {animal["characteristics"]["type"]}\n"
    output += f"\n"


output_2 = ""  # define an empty string
for animal in animals_data:
    # append information to each string
    output_2 += '<li class="cards__item">'
    output_2 += f"Name: {animal["name"]}<br/>\n"
    output_2 += f"Diet: {animal["characteristics"]["diet"]}<br/>\n"
    output_2 += f"Location: {", ".join(animal["locations"])}<br/>\n"
    if "type" in animal["characteristics"]:
        output_2 += f"Type: {animal["characteristics"]["type"]}<br/>\n"
    output_2 += f"<br/>\n"
    output_2 += "</li>"



output_3 = ""  # define an empty string
for animal in animals_data:
    # append information to each string
    output_3 += '<li class="cards__item">'
    output_3 += f'<div class ="card__title"> {animal["name"]} <br/>\n</div>'
    output_3 += f'<p class="card__text">'
    output_3 += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]} <br/>"
    output_3 += f"<strong>Location:</strong> {", ".join(animal["locations"])} <br/>\n"
    if "type" in animal["characteristics"]:
        output_3 += f"<strong>Type:</strong> {animal["characteristics"]["type"]} <br/>\n"
    output_3 += "</p>"
    output_3 += "</li>"


'''export'''
text = output_2
text_update = text.replace(text, output_3)

with open("animals_template.html", "r") as file:
    html_content = file.read()

update_content = html_content.replace(text, text_update)

with open("animals_template.html", "w", encoding="utf-8") as file:
    file.write(update_content)


print("HTML file updated successfully!")













