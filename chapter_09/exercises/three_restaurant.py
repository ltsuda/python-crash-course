class Restaurant:
    """Simple model of a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.name = name
        self.cuisine_type = cuisine_type

    def description(self):
        """Describe the restaurant"""
        print(f"The restaurant name is {self.name}"
              f" and its serves {self.cuisine_type} food")

    def open(self):
        """Print a message that the restaurant is open"""
        print(f"The {self.name} restaurant is open!")


jp_restaurant = Restaurant('Sushi Dojo', 'Japonese')
pizza_restaurant = Restaurant('The pizza place', 'Pizza')
outback_restaurant = Restaurant('Outback', 'Australian')

jp_restaurant.description()
jp_restaurant.open()
pizza_restaurant.description()
pizza_restaurant.open()
outback_restaurant.description()
outback_restaurant.open()
