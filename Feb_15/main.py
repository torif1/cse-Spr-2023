"""Main place to test classes from resteraunt2"""
from resteraunt3 import *
from car import *


#Try it yourself 1
Timmothies=IceCreamStand('Timothies')
print(Timmothies.describe_flavors())
print(Timmothies.describe_resteraunt())


print('Try it yourself 2:')
#Try it yourself 2
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.battery.get_range())
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())