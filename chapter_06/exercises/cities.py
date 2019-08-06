cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}

for city, info in cities.items():
    print(f"{city.title()} is located at {info['country'].title()}, "
          f"its population are {info['population']} and "
          f"the nearby mountain is {info['nearby mountains'].title()}.")
