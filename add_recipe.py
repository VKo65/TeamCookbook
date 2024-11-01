
# var:  name, ingredients, and instructions
import json

# Load data from JSON file and assign to a variable
with open('recipes.json', 'r') as file:
    cookbook = json.load(file)

# Now you can use cookbook as your variable
print(cookbook)


#def add_recipe():
