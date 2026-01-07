import json

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

animals_string_data = ""

for animal in animals_data:
    animals_string_data += '<li class="cards__item">\n'

    # Name
    if "name" in animal:
        animals_string_data += f"Name: {animal['name']}<br/>\n"

    # Diet
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_string_data += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    # Locations (first one only)
    if "locations" in animal and animal["locations"]:
        animals_string_data += f"Locations: {animal['locations'][0]}<br/>\n"

    # Type
    if "characteristics" in animal and "type" in animal["characteristics"]:
        animals_string_data += f"Type: {animal['characteristics']['type']}<br/>\n"

    animals_string_data += "</li>\n\n"

with open("animals_template.html", "r", encoding="utf-8") as file:
    template_content = file.read()

print(template_content)

template_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_string_data)
print(template_content)


with open("animals.html", "w", encoding="utf-8") as f:
    f.write(template_content)