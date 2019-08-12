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

    def fill_gas_tank(self):
        """Electric car don't have gas tanks."""
        print("This car doesn't need a gas tank!")


class Battery:
    """A simple attempt to model a battery size."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print the battery size of the electric car."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade battery capacity."""
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes from the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()
