"""A class the can be used to represent gas and electric cars."""


class Car:
    """Representation of a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes that describes a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        description = (f"{self.year} {self.manufacturer.title()} "
                       f"{self.model.title()}")

        return description

    def read_odometer(self):
        """Return the car mileage."""
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to the given value."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increment the mileage."""
        if miles >= self.odometer:
            self.odometer += miles
        else:
            print("You can't roll back an odometer!")
