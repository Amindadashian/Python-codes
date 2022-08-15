hour=int(input('how many hours--> '))
rate=int(input('how much rate--> '))
gross=hour*rate
tax=gross*0.1
netsalary=gross-tax
print('gross = ',gross)
print('tax =',tax)
print('net salary = ',netsalary)

