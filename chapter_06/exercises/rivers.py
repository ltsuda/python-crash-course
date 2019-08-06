rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, location in rivers.items():
    print(f"The {river.title()} river runs through {location.title()}.")

for river in rivers.keys():
    print(f"The river {river.title()} in this dictionary.")

for location in rivers.values():
    print(f"The river in this dictionary are located in {location.title()}.")
