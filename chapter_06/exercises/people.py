person_0 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 28,
    'city': 'New York'
}
person_1 = {
    'first_name': 'Mike',
    'last_name': 'Patt',
    'age': 19,
    'city': 'Paris'
}
person_2 = {
    'first_name': 'Lisa',
    'last_name': 'Yung',
    'age': 22,
    'city': 'New Zealand'
}

people = [person_0, person_1, person_2]

for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    age = f"{person['age']}"
    city = f"{person['city']}"
    print(f"{name.title()}, of {city.title()}, is {age} years old")
