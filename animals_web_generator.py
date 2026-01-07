import json

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def serialize_animal(animal):
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'<div class="card__title">{animal["name"]}</div>\n'

    output += '<p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '</p>\n'
    output += '</li>\n'

    return output

animals_data = load_data("animals_data.json")

animals_string_data = ""

for animal in animals_data:
    animals_string_data += serialize_animal(animal)

with open("animals_template.html", "r", encoding="utf-8") as file:
    template_content = file.read()

template_content = template_content.replace(
    "__REPLACE_ANIMALS_INFO__", animals_string_data
)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(template_content)