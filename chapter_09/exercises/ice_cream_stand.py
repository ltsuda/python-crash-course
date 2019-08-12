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


class IceCreamStand(Restaurant):
    """A simple model of a ice scream stand"""

    def __init__(self, name, cuisine_type, flavors, number_served=0):
        super().__init__(name, cuisine_type, number_served)
        self.flavors = flavors

    def available_flavors(self):
        """Print a list of flavors available."""
        for flavor in self.flavors:
            print(f'We have {flavor} flavor available.')


ice_cream_stand = IceCreamStand('Ice Cream Place', 'Ice Cream', [
                                'chocolate', 'strawberry', 'cream'])
ice_cream_stand.description()
ice_cream_stand.open()
ice_cream_stand.set_number_served(1)
ice_cream_stand.increment_number_served(5)
ice_cream_stand.available_flavors()
print(ice_cream_stand.number_served)
