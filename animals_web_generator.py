import json

# original HTML-file
HTML_TEMPLATE_FILE = "animals_template.html"
# file which will be overwritten
OUTPUT_HTML_FILE = "index.html"


with open("animals_data.json", "r", encoding="utf-8") as file:
    animals_data = json.load(file)


skin_types = set()
for animal in animals_data:
    if "skin_type" in animal["characteristics"]:
        skin_types.add(animal["characteristics"]["skin_type"])


while True:
    print("Available skin types:")
    for skin in sorted(skin_types):
        print(f"- {skin}")

    selected_skin_type = input("\nEnter a skin type from the list above or hit enter to show all types: ").strip().lower()

    if selected_skin_type == "":
        filtered_animals = animals_data
        break
    elif selected_skin_type in ("fur", "hair", "scales"):
        filtered_animals = []
        for animal in animals_data:
            if "skin_type" in animal["characteristics"] and animal["characteristics"]["skin_type"].lower() == selected_skin_type:
                filtered_animals.append(animal)
        break

    else:
        print("Invalid Input, please choose from the list.")



def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]} <br/>"
    output += f"<strong>Location:</strong> {", ".join(animal["locations"])} <br/>\n"
    if "skin_type" in animal["characteristics"]:
        output += f"<strong>Skin Type:</strong> {animal["characteristics"]["skin_type"]} <br/>\n"

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
for animal in filtered_animals:  #
    output += serialize_animal(animal)


#export
text = "__REPLACE_ANIMALS_INFO__"
text_update = text.replace(text, output)

with open(HTML_TEMPLATE_FILE, "r", encoding="utf-8") as file:
    html_content = file.read()

update_content = html_content.replace(text, text_update)

with open(OUTPUT_HTML_FILE, "w", encoding="utf-8") as file:
    file.write(update_content)

print("HTML file updated successfully!")