"""Main place to test classes from resteraunt2"""
from resteraunt2 import Resteraunt

Anthonies=Resteraunt('Anthonies','Shell Fish')
Anthonies.set_number_served(3)
print(Anthonies.customersserved)
Anthonies.incrament_number_served(5)
print(Anthonies.customersserved)
