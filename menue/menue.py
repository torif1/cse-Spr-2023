#Imports
import menufunctions as mf

total=0
discount=0

sandwich_lst=[]
beverage_lst=[]
fries_lst=[]

while True:
    total,sandwich_lst=mf.get_Sandwich(total, sandwich_lst)
    total,beverage_lst=mf.get_Beverage(total,beverage_lst)
    total,fries_lst=mf.get_french_fries(total,fries_lst)

    user_done=str(input('Is that all?')).lower()
    while user_done=='no':
        mf.get_Sandwich(total,sandwich_lst)
        mf.get_Beverage(total,beverage_lst)
        mf.get_french_fries(total,fries_lst)
        user_done=bool(input('Is that all?'))

    total, packets=mf.get_ketchup(total)
        
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
