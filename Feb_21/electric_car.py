from car import Car


class Battery():
    def __init__(self):
        self.battery_size = 75

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        return range

    def upgrade_battery(self):
        self.battery_size = 100

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
