def salary(hours,per_hour):
    salary = hours*per_hour
    if hours > 8:
        return ('error')

    else:
        return salary


hours = int(input("please enter hours => "))
print(salary(hours,4))

    













