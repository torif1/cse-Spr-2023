"""User Class"""
class User:
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.lastname=last_name

    def describe_user(self):
        print(f"first name={self.firstname} last name={self.lastname}")

    def greet_user(self):
        print(f"Hello {self.firstname}!")