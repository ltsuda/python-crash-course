pet_0 = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pet_1 = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pet_2 = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    animal_type = f"{pet['animal type']}"
    name = f"{pet['name']}"
    owner = f"{pet['owner']}"
    weight = f"{pet['weight']}"
    eats = f"{pet['eats']}"
    print(f"{owner.title()} is the owner of this {animal_type}, named "
          f"{name.title()}. {name.title()} weights {weight} and eats {eats}")
