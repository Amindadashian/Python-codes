#a=numbers      temp=variable temporary

a=int(input('enter a =  '))    
b=int(input('enter b =  '))
c=int(input('enter c =  '))
if a>b :
    temp=a
    a=b
    b=temp
if a>c:
    temp=a
    a=c
    c=temp
if b>c:
    temp=b
    b=c
    c=temp
print('sorted is :',a,b,c)