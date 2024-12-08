import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_string(animals):
    output = ''
    for animal in animals:
        output += f"Name: {animal.get('name', '')}\n"

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}\n"

        if 'locations' in animal and animal['locations']:
            output += f"Location: {animal['locations'][0]}\n"

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"

        output += "\n"  # Leere Zeile zwischen den Tieren

    return output


# JSON-Datei laden
file_path = 'animals_data.json'
animals_data = load_data(file_path)

# Tierdaten als String generieren
animal_string = generate_animal_string(animals_data)

# HTML-Vorlage lesen
with open('animals_template.html', 'r') as template_file:
    template_content = template_file.read()

# Tierdaten in die Vorlage einfügen
final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_string)

# Finale HTML in eine neue Datei schreiben
with open('animals.html', 'w') as final_file:
    final_file.write(final_html)

print("HTML-Datei wurde erfolgreich erstellt: animals.html")