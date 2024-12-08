import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_animal_string(animals):
    output = ''
    for animal in animals:
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal.get("name", "")}</div>\n'
        output += '  <p class="card__text">\n'

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

        if 'locations' in animal and animal['locations']:
            output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output


# JSON-Datei laden
file_path = 'animals_data.json'
animals_data = load_data(file_path)

# Tierdaten als HTML-String generieren
animal_html = generate_animal_string(animals_data)

# HTML-Vorlage lesen
with open('animals_template.html', 'r') as template_file:
    template_content = template_file.read()

# Tierdaten in die Vorlage einfügen
final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_html)

# Finale HTML in eine neue Datei schreiben
with open('animals.html', 'w') as final_file:
    final_file.write(final_html)

print("HTML-Datei wurde erfolgreich erstellt: animals.html")