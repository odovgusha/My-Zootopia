import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

animals_string_data = ''

for animal in animals_data:
    if "name" in animal:
        #animal_name = (animal["name"])
        print(f"Name: {animal["name"]}")
        animals_string_data += f"Name: {animal['name']}\n"

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            animal_diet = animal["locations"][0] = animal["characteristics"]["diet"]
            print(f"Diet: {animal_diet}")
            animals_string_data += f"Diet: {animal_diet}\n"

    if "locations" in animal and animal["locations"]:
        animal_locations = animal["locations"][0]
        print(f"Locations: {animal_locations}")
        animals_string_data += f"Locations: {animal_locations}\n"

    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            print(f"Type: {animal["characteristics"]["type"]}")
            animals_string_data += f"Type: {animal['characteristics']['type']}\n"
    print("\n")
    animals_string_data += "\n"
    """
        print(
        f"Name: {animal_name}\n"
        f"Diet: {animal_diet}\n"
        f"Locations: {animal_locations}\n"
        f"Type: {animal_type}\n"
    )
    """

with open("animals_template.html", "r", encoding="utf-8") as file:
    template_content = file.read()

print(template_content)

template_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_string_data)
print(template_content)


with open("animals.html", "w", encoding="utf-8") as f:
    f.write(template_content)