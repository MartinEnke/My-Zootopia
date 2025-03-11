
def export_html_file(template_file, output_file, content_update):
    '''
    Replaces the requested content with the placeholder
    and exports the updated page as index.html
    '''
    placeholder = "__REPLACE_ANIMALS_INFO__"

    with open(template_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    update_content = html_content.replace(placeholder, content_update)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(update_content)

    print("HTML file updated successfully!")