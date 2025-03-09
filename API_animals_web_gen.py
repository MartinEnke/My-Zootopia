import requests

# original HTML-file
HTML_TEMPLATE_FILE = "animals_template.html"
# file which will be overwritten
OUTPUT_HTML_FILE = "index.html"


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


def create_website(output):

    #export
    text = "__REPLACE_ANIMALS_INFO__"
    text_update = text.replace(text, output)

    with open(HTML_TEMPLATE_FILE, "r", encoding="utf-8") as file:
        html_content = file.read()

    update_content = html_content.replace(text, text_update)

    with open(OUTPUT_HTML_FILE, "w", encoding="utf-8") as file:
        file.write(update_content)


def main():
    animal = input("Enter animal name: ")
    API_KEY = "Sxt9ncDQfyLYr5YnqVXY3w==AiT3mSC1ktGYGWbp"
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    response = requests.get(api_url, headers={"X-API-KEY": API_KEY})

    if response.status_code == requests.codes.ok:
        animals_data = response.json()

        if not animals_data:
            output = f"<p style='color:red;'>The animal {animal} does not exist in the database</p>"
            print(f"The animal {animal} does not exist in the database")

        else:
            output = ""
            for animal in animals_data:
                output += serialize_animal(animal)
        create_website(output)
        print("HTML file updated successfully!")

if __name__ == "__main__":
    main()

