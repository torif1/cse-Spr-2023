import resteraunt
from resteraunt import Resteraunt
from resteraunt import *


resteraunt1=Resteraunt('Anthonies','Pizza')
resteraunt2=Resteraunt('Chipolte','Mexican')
resteraunt3=Resteraunt('Burger King', 'Burgers')

for resteraunt in [resteraunt1,resteraunt2, resteraunt3]:
    resteraunt.describe_resteraunt()

user1=User('Harold',"Huccaby")
user2=User('Jamie','Jones')
user3=User('Tod', 'Todders')

for user in [user1, user2 ,user3]:
    user.describe_user()
    user.greet_user()