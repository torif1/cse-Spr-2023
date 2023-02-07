#Imports
import menufunctions
from menufunctions import *

total=0
discount=0

#I guess I need to find a way to add different things to the list.


#defining dictionarys to avoid if else statements
sandwichdict = {'chicken':5.25,'beef':6.25,'tofu':5.75}
beveragedict = {'small':1,'medium':1.75,'large':2.25}
friesdict    = {'small':1,'medium':1.5,'large':2}

sandwich_lst=[]
beverage_lst=[]
fries_lst=[]

while True:
    total,sandwich_lst=get_Sandwich(total, sandwich_lst)
    total,beverage_lst=get_Beverage(total,beverage_lst)
    total,fries_lst=get_french_fries(total,fries_lst)

    user_done=str(input('Is that all?')).lower()
    while user_done=='no':
        get_Sandwich(total,sandwich_lst)
        get_Beverage(total,beverage_lst)
        get_french_fries(total,fries_lst)
        user_done=bool(input('Is that all?'))

    total, packets=get_ketchup(total)
        
    if ((len(sandwich_lst)>=1) and (len(fries_lst)>=1) and (len(beverage_lst)>=1)):
        total=total-1
    print('\n', '\n', '\n','Your Order:')
    print('Sandwiches:')
    for li in sandwich_lst:
        print(li)
    print('Beverages:')
    for li in beverage_lst:
        print(li)
    print('Fries:')
    for li in fries_lst:
        print(li)
    print("katchup packets:",packets)
    print('Total:',total)

    print('\n New Order:')
