# Question 1: Create an empty set called my_ints, once it's created
# use the type function (along with print) to print the type of my_ints.
## Write your code below, 2 lines
my_ints = set()
print(type(my_ints))
#Question 2: Given the list below, convert it to a set named my_set and then
# cast it back to a list called my_unique_list which only includes unique
# elements. No print required.
my_list = [1,1,'rails',7,6,2,'java','ruby',8,9,10,21,'rails',7,2,1000,6,'python','java']
## Write your code below, 2 lines
my_set =set(my_list)
print(my_set)
my_unique_list = list(my_set)
print(my_unique_list)
#Question 3: Add the int 8 to my_ints you created in question 1. Print the
# output when you run the intersection method on my_ints and pass it my_set
# (created in question 2) as the argument.
## Write your code below, 2 lines
my_unique_list
my_ints.add(8)
print(my_ints.intersection(my_set))
#Question 4: Test (and print) if 'rails' is in my_set
## Write your code below, 1 line
print('rails'in my_set)

#Question 5: Given the tuple below, use a simple for loop and print out all
# the elements in it (no special formatting).
my_random_tuple = ('first',4,5,8,'hi there',5,2,1,9,10)
for item in my_random_tuple:
    print(item)


