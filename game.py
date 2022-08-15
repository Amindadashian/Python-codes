
import random
print('-'*20,'WWWEEELLLCCCOOOMMM','-'*20)
computer_name= 'Dani'
user_name= input('please inter your name---->    ')
print('my name is Dani and i send warm hello to you dear',user_name)
computer_choice =random.randint(1,10)
print('computer_choice = ',computer_choice)
your_choice = int(input('inter your number---->   '))
#print('your choice is --->',your_choice)
computer_score= 0
while computer_choice != your_choice:
    if computer_choice < your_choice:
        #print('computer number is smaller than your choice')
        print('K')
    else:
        #print('computer number is bigger than your choice ')
        print('B')
    computer_choice=random.randint(1,10)

print('your choice is --->',your_choice)
#print('yeeeeeessssss',computer_name,'I did it')
print('D')








