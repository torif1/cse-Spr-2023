import restaurant
from restaurant import *


restaurant1=Restaurant('Anthonies','Pizza')
restaurant2=Restaurant('Chipolte','Mexican')
restaurant3=Restaurant('Burger King', 'Burgers')

for restaurant in [restaurant1,restaurant2, restaurant3]:
    restaurant.describe_restaurant()

user1=User('Harold',"Huccaby")
user2=User('Jamie','Jones')
user3=User('Tod', 'Todders')

for user in [user1, user2 ,user3]:
    user.describe_user()
    user.greet_user()
