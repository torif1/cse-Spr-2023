"""Car class and subclasses"""
class Car:
    def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year
           self.odometer_reading = 0
    def get_descriptive_name(self):
           long_name = f"{self.year} {self.make} {self.model}"
           return long_name.title()
    def read_odometer(self):
           print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()

class Battery():
    def __init__(self):
         self.battery_size=75

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        return range
    
    def upgrade_battery(self):
        self.battery_size=100

    print(f"This car can go about {range} miles on a full charge.")
