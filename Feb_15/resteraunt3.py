"""resteraunt class and subclasses"""

class Resteraunt:
    def __init__(self, resteraunt_name, cuisine_type):
        self.name=resteraunt_name
        self.foodtype=cuisine_type
        self.open='False'
        self.customersserved=0

    def describe_resteraunt(self):
        print(f'foodtype={self.foodtype} and name={self.name}')

    def open_resteraunt(self):
        print('This Resteraunt is Open')

    # Defining a method to set number of guests served
    def set_number_served(self,guests_served):
        guests_served: int>0
        if guests_served>0:
            self.customersserved+=int(guests_served)
        else:
            print('Must update by a positive integer')

    #Defining method to incament guests served by input value
    def incrament_number_served(self,incrament_value):
        incrament_value: int>0
        self.customersserved+=int(incrament_value)

class IceCreamStand(Resteraunt):
    def __init__(self,resteraunt_name):
        super().__init__(self,resteraunt_name)
        self.flavors=['chocolate', 'vanila','serbet']
        self.foodtype='Icecream'
        self.name=resteraunt_name

    def describe_flavors(self):
        print(f'Icecream flavors are:{self.flavors}')



