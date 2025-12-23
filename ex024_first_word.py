city = input("Enter a city name: ").strip().upper()
city_split = city.split()

print(f"The city name starts with SANTO? {'SANTO' in city_split[0]}.")
