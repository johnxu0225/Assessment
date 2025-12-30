from weather_api import get_weather
from favorites import FavoritesManager


def display_weather(weather):
    #Print formatted weather details
    print(f"\nCity: {weather['city']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Weather: {weather['description']}\n")


def search_weather():
    #Submenu: search weather repeatedly until user goes back
    while True:
        city = input("Enter city name (or 'b' to go back): ")
        if city.lower() == 'b':
            return
        weather = get_weather(city)
        if weather:
            display_weather(weather)
        else:
            print("City not found.")


def add_favorite(favorites_manager):
    #Submenu: add favorite cities until user goes back
    while True:
        city = input("Enter city to add (or 'b' to go back): ")
        if city.lower() == 'b':
            return
        print(favorites_manager.add_city(city))


def remove_favorite(favorites_manager):
    #Submenu: remove city from favorites
    while True:
        city = input("Enter city to remove (or 'b' to go back): ")
        if city.lower() == 'b':
            return
        print(favorites_manager.remove_city(city))


def list_favorites(favorites_manager):
    #List all favorites with current weather
    cities = favorites_manager.list_cities()
    if not cities:
        print("No favorite cities yet.")
        return
    for city in cities:
        weather = get_weather(city)
        if weather:
            display_weather(weather)


def main():
    favorites_manager = FavoritesManager()

    while True:
        #Main menu
        print("\n--- Weather App ---")
        print("1. Search weather")
        print("2. Add favorite")
        print("3. List favorites")
        print("4. Remove favorite")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_weather()  #enter search submenu
        elif choice == "2":
            add_favorite(favorites_manager)  #enter add submenu
        elif choice == "3":
            list_favorites(favorites_manager)
        elif choice == "4":
            remove_favorite(favorites_manager)  #enter remove submenu
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
