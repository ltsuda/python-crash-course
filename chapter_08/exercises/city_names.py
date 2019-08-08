def city_country(city, country):
    """ Returns a city and country, neatly formatted. """
    city_country = f"{city}, {country}."

    return city_country.title()


city_and_country = city_country('Campinas', 'Brazil')
print(city_and_country)
city_and_country = city_country('Calgary', 'Canada')
print(city_and_country)
city_and_country = city_country('San Francisco', 'United States')
print(city_and_country)
