from car import Car
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle=Car('Volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#I have been doing most of this already
#Look at Feb_15 for try it yourself, as it has already been done