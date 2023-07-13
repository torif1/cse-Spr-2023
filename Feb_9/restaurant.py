class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name=restaurant_name
        self.foodtype=cuisine_type
        self.open='False'
    
    def describe_restaurant(self):
        print(f'foodtype={self.foodtype} and name={self.name}')

    def open_restaurant(self):
        print('This restaurant is Open')

class User:
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.lastname=last_name
    
    def describe_user(self):
        print(f"first name={self.firstname} last name={self.lastname}")

    def greet_user(self):
        print(f"Hello {self.firstname}!")
