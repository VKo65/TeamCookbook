from cookbook_storage import get_cookbook_data, write_cookbook_data


def cookbook_menu() -> None:
    """
    Listener Loop which prints the menu and lets User choose a function to use.
    TODO: Implement functionality, need to talk with teamleader for assignment.
    :return: None
    """
    function_dict = {
        "1": {
            "function": list_recipes,
            "name": "List all recipes"
        },
        "2": {
            "function": display_recipe,
            "name": "Search for specific recipe"
        },
        "3": {
            "function": adding_recipe,
            "name": "Add new recipe"
        },
    }
    pass


# assigned member: Chris
def adding_recipe():
    """
    Recipe Adding Functionality - Create a function that
    takes user input for a recipe name, ingredients, and instructions and
    parses it to write_cookbook_data().
    :return:
    """
    pass

# assigned member: Felipe
def list_recipes() -> None:
    """
    Uses get_cookbook_data() to get all data and prints out every entry by name and a short description.
    :return: None
    """
    pass

# assigned member: Suti
def search_recipes(cookbook_data: list) -> int:
    """
    Prompts User to enter a search term, and searches for matches in given list.
    If found returns it's Index
    :return: int
    """
    pass

# assigned member: Kenneth
def display_recipe() -> None:
    """
    Calls search_recipes() to get index of desired recipe and prints out all details.
    :return: None
    """
    cookbook_data = get_cookbook_data()
    recipe_index = search_recipes()

    recipe_name = cookbook_data[recipe_index]["Name"]
    recipe_ingredients = cookbook_data[recipe_index]["Ingredients"]
    recipe_instructions = cookbook_data[recipe_index]["Instructions"]

    print(f"{recipe_name}\nIngredients: {recipe_ingredients}\nInstructions: {recipe_instructions}\n")


def main():
    pass


if __name__ == "__main__":
    main()
