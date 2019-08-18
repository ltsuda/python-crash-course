import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename, 'r') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input(f"What's your name? ")
    filename = 'username.json'

    with open(filename, 'w') as file:
        json.dump(username, file)

    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.capitalize()}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}.")


greet_user()
