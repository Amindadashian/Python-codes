from itertools import count


s=input('enter the string---> ')
sound='e,i,u,o,'
count=0
for i in s:
    if i in sound:
        count=count+1
print('count is ',count)