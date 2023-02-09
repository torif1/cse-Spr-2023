class Resteraunt:
    def __init__(self, resteraunt_name, cuisine_type):
        self.name=resteraunt_name
        self.foodtype=cuisine_type
        self.open='False'
    
    def describe_resteraunt(self):
        print(f'foodtype={self.foodtype} and name={self.name}')

    def open_resteraunt(self):
        print('This Resteraunt is Open')

class User:
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.lastname=last_name
    
    def describe_user(self):
        print(f"first name={self.firstname} last name={self.lastname}")

    def greet_user(self):
        print(f"Hello {self.firstname}!")
