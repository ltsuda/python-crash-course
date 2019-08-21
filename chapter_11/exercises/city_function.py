def get_formatted_city(city, country, population=None):
    """Generate a neatly formatted city and country name."""
    if population:
        city_country = f"{city.title()}, {country.title()} - population {population}."
    else:
        city_country = f"{city.title()}, {country.title()}."

    return city_country
