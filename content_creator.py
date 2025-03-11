def serialize_animal(animal):
    """Generates an HTML snippet for a given animal."""
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


def html_update(filtered_animals):
    """Generate HTML for all filtered animals."""
    output = ''
    for animal in filtered_animals:  #
        output += serialize_animal(animal)
    return output
