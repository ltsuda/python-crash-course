import json


filename = 'exercises/favorite_number.json'
with open(filename, 'r') as file:
    favorite_number = json.load(file)

print(f"Your favorite number is {favorite_number}")
