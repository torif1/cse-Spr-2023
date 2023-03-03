num1=input('What is your first number?')
num2=input('What is your second number?')
try:
    num_sum=int(num1)+int(num2)
except:
    print("Sorry, one of the numbers you entered is in fact not a number!")
else:
    print(f'sum:{num_sum}')