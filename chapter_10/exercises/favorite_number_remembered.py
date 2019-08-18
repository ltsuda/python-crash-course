import json


def get_stored_number():
    """Get stored number if available."""
    filename = 'exercises/number.json'

    try:
        with open(filename, 'r') as file:
            number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    """Prompt for a new number."""
    number = input(f"What's your favorite number? ")
    filename = 'exercises/number.json'

    with open(filename, 'w') as file:
        json.dump(number, file)

    return number


def ask_favorite_number():
    """Greet the user by name."""
    number = get_stored_number()
    if number:
        print(f"Welcome back, your favorite number is {number}")
    else:
        number = get_new_number()
        print(
            f"We'll remember your favorite number when you are back.")


ask_favorite_number()
