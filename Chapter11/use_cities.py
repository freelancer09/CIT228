from city_functions import get_formatted_city

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease enter a city: ")
    if city == 'q':
        break
    country = input("Please enter a country: ")
    if country == 'q':
        break
    population = input("Please enter the population: ")
    if population == 'q':
        break
    formatted_city = get_formatted_city(city,country,population)
    print(f"\tFormatted City Information: {formatted_city}.")