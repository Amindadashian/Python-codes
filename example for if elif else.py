
import random
random.randint(1,10)
name = input('plese inter your name --->    ')
answer = random.randint(1,10)
guess = int(input("what is your number ----->   "))

while guess != answer:
    if guess < answer :
        print('your guess is smaller than answer :( ')
    else :
        print("your guess is larger than answer :(")
    guess = int(input("what is your number ----->   "))

print('yessssss',name,'you did it  :DD ')



