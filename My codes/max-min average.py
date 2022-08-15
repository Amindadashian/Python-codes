
id1=-1
max1=-1
max2=-1
id2=-1
n=int(input('enter tedad = '))
if n< 2:
    print('please inter a number greater than 1.')
else:
    for i in range(1,n+1):
        id=int(input('enter id:'))
        average=float(input('inter average : '))
    if average > max1:
        id2=id1
        max2=max1
        id1=id
    else:
        if average> max2:
            max2=average
            id2=id
print('max2 =',max2,'\t','id2=',id2)







