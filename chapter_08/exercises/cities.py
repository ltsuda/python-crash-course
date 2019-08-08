def describe_city(city_name, country='Canada'):
    """ Display information about a city. """
    print(f"{city_name.title()} is in {country.title()}")


describe_city(country='EUA', city_name='New York')
describe_city(city_name='Calgary')
describe_city('Vancouver')
