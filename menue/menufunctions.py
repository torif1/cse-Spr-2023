def get_Sandwich(totalcost,sandwich_lst):
    typesandwich = str(input('What type of sandwich?')).lower()
    if typesandwich == 'chicken' or 'beef' or 'tofu':
        totalcost+=sandwichdict[typesandwich]
        sandwich_lst.append(typesandwich)
    else:
        print('invalid')
    return totalcost,sandwich_lst

def get_Beverage(totalcost,beverage_lst):
    beverageyn   = str(input('Would you like a beverage?')).lower()
    if beverageyn=='yes':
        beverage=str(input('What size beverage?')).lower()
        if beverage in beveragedict:
            totalcost+=beveragedict[beverage]
            beverage_lst.append(beverage)
        else:
            print('invalid')
    return totalcost, beverage_lst

def get_french_fries(totalcost,fries_lst):
    frenchfries  =str(input('Would you like Fries?')).lower()
    if frenchfries=='yes':
        fries=str(input('What size of fries?')).lower()
        if fries=='small':
            temp=str(input('Would you like to mega-size your fries?')).lower()
            if temp=='yes':
                totalcost+=2
                fries='megafries'
            else:
                totalcost+=friesdict[fries]
        fries_lst.append(fries)
    return totalcost, fries_lst

def get_ketchup(totalcost):
    packets=int(input('How many katchup packets would you like?'))
    totalcost=packets * .25 + totalcost
    return totalcost, packets