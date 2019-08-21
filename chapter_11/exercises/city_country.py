from city_function import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city == 'q':
        break
    country = input("\nPlease give me the country where the city is located: ")
    if country == 'q':
        break

    formatted_city = get_formatted_name(city, country)
    print(f"\tNeatly formatted city location: {formatted_city}.")
