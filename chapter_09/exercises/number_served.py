class Restaurant:
    """Simple model of a restaurant."""

    def __init__(self, name, cuisine_type, number_served=0):
        """Initialize restaurant name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def description(self):
        """Describe the restaurant."""
        print(f"The restaurant name is {self.name}"
              f" and its serves {self.cuisine_type} food")

    def open(self):
        """Print a message that the restaurant is open."""
        print(f"The {self.name.title()} restaurant is open!")

    def set_number_served(self, customer_served):
        """Set the number of customer served."""
        self.number_served = customer_served

    def increment_number_served(self, number):
        """Increment the number of customer serverd."""
        if number > 0:
            self.number_served += number
        else:
            print("You can't reduce the number of served customer"
                  "with this method.")


my_restaurant = Restaurant('Sushi Dojo', 'Japonese')
my_restaurant.description()
my_restaurant.open()

restaurant = Restaurant('Temakeria', 'Temaki')
print(f"We have served {restaurant.number_served} customers.")
restaurant.number_served = 1
print(f"We have served {restaurant.number_served} customers.")
restaurant.set_number_served(10)
print(f"We have served {restaurant.number_served} customers.")
restaurant.increment_number_served(100)
print(f"We have served {restaurant.number_served} customers.")
