from car import Car
from electric_car import ElectricCar as EC

my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())
my_car.odometer = 23
my_car.update_odometer(24)
my_car.update_odometer(20)
my_car.increment_odometer(100)
my_car.read_odometer()

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
