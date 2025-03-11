from get_data import get_animal_data
from user_filter import user_filter
from content_creator import html_update
from export import export_html_file


ANIMALS_JSON = "animals_data.json"
# original HTML-file
HTML_TEMPLATE_FILE = "animals_template.html"
# file which will be overwritten
OUTPUT_HTML_FILE = "index.html"


def main():
    # Load data
    animals_data = get_animal_data(ANIMALS_JSON)
    # Filter by skin type
    filtered_animals = user_filter(animals_data)
    # Generate HTML content
    update_content = html_update(filtered_animals)
    # Update HTML page
    export_html_file(HTML_TEMPLATE_FILE, OUTPUT_HTML_FILE, update_content)

if __name__ == "__main__":
    main()


