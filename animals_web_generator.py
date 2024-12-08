import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animals):
    for animal in animals:
        print(f"Name: {animal.get('name', '')}")

        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")

        if 'locations' in animal and animal['locations']:
            print(f"Location: {animal['locations'][0]}")

        if 'characteristics' in animal and 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")

        print()  # Print an empty line between animals


file_path = 'animals_data.json'

animals_data = load_data(file_path)

print_animal_info(animals_data)

