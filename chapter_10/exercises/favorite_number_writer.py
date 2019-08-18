import json

favorite_number = input(f"What's your favorite number? ")

filename = 'exercises/favorite_number.json'
with open(filename, 'w') as file:
    json.dump(favorite_number, file)
