"""Main place to test classes from restaurant2"""
from restaurant2 import Restaurant

Anthonies=Restaurant('Anthonies','Shell Fish')
Anthonies.set_number_served(3)
print(Anthonies.customersserved)
Anthonies.incrament_number_served(5)
print(Anthonies.customersserved)
