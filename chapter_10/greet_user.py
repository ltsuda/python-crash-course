import json


filename = 'username.json'
with open(filename, 'r') as file:
    username = json.load(file)
    print(f"Welcome back, {username.capitalize()}")
