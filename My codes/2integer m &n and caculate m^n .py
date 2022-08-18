#m=base پایه
#n=power  توان
#i=  1,n-1
#j=  1,m  یک تا ام 
#sum= total (در پایان مقدارتوان قرار گیرد)
#temp=assistant variuable (برای نگهداری مجموع هر دوره)
m=int(input('enter n: '))
n=int(input('inter n: '))
sum=0
temp=m
for i in range(1,n):
    sum=0
    for j in range(1,m+1):
        sum=sum+temp
    temp=sum
print(m," ^ ",n," = ",sum)
