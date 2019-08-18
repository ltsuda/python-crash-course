import json


filename = 'numbers.json'
with open(filename, 'r') as file:
    numbers = json.load(file)

print(numbers)
