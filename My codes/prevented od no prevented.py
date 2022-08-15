from re import I


while True:
    num=int(input('please enter your number : '))
    sum=0
    for i in range(1,num):
        if (num % i ==0):
            sum +=i 
    if (sum == num):
        print('/t','prefected')
    else:
        print('/t','not prefected')
    yes=input('continue?? ')
    if (yes=='no' or yes=='n'):
        break