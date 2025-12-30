MAX_FAVORITES = 3  #Maximum allowed favorite cities

class FavoritesManager:
    def __init__(self):
        self.favorites = []  #Store favorite cities in list

    def add_city(self, city):
        #Prevent duplicate cities
        if city in self.favorites:
            return "City already in favorites."

        #Enforce max favorites limit
        if len(self.favorites) >= MAX_FAVORITES:
            return "You can only have 3 favorite cities."

        #Add city to favorites
        self.favorites.append(city)
        return "City added to favorites."

    def remove_city(self, city):
        #Check if city exists before removing
        if city not in self.favorites:
            return "City not found in favorites."

        #Remove city
        self.favorites.remove(city)
        return "City removed."

    def list_cities(self):
        #Return all favorite cities
        return self.favorites
