import json
test
FILEPATH = "cookbook_database.json"

# assigned member: Felipe
def get_cookbook_data() -> list:
    """
    Opens the JSON file and returns data as python datastructure.
    :return: list
    """
    pass

# assigned member: Chris
def write_cookbook_data(new_data: list) -> None:
    """
    Writes given data into the JSON file.
    :param new_data: list
    :return: None
    """
    pass

# following three functions are not needed if we provide a JSON with default data.
def write_default_data() -> None:
    """
    Creates JSON file with default data.
    :return:
    """
    pass


def validate_existence() -> bool:
    """
    Checks if the file exists, if data
    does not exist function calls write_default_data().
    :return: Bool
    """
    pass


def validate_data() -> bool:
    """
    Calls validate_existence() to check if there is any data,
    if there is data to work with it reads the data and checks
    if data is valid. In case data is invalid it calls write_default_data().
    :returns: Boolean
    """
    pass