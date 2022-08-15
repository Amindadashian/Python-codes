number =int(input('please input your number: '))
if number > 1 :
    for i in range( 2 , int(number/2)+1 ):
        if (number % i) == 0 :
            print('not prime')
            break
    else:
        print('prime')

else:
    print('your number is not prime')



