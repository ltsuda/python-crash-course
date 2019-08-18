import json

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

filename = 'numbers.json'
with open(filename, 'w') as file:
    json.dump(numbers, file)
