favorite_numbers = {
    'Conan': [10, 20, 30, 40],
    'Radhika': [8, 18, 28],
    'Dalia': [95],
    'Mark': [83, 103, 123],
    'Khalil': [74]
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
