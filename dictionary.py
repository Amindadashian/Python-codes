
from multiprocessing.sharedctypes import Value


my_dictionary = {'name': 'mashrur' ,'course' : 'python','fave_food' : 'ice cream'}
phone_dict = {'mashrur' : '933-300-36-22',
'zoolander' : '999-888-777',
'jon_snow' : 'fail-o-so-bad'}
word_dict = {'a':
 {
 'apple': 'the round fruit of a tree of the rose family',
 'ant': 'an insect which cleans up the floor'
 },
 'b':
 {
 'bad': 'of poor quaity or low standard',
 'business': 'season 8 of GOT'
 }
 }

my_dictionary['name'] = 'john'
#print(my_dictionary)
my_dictionary['job'] = 'python programer'
#print(my_dictionary)
#print(word_dict['b']['business'])
#print(word_dict['a']['apple'])
#print(my_dictionary.keys())
#print(my_dictionary.values())
#print(my_dictionary.items())
for key, Value in my_dictionary.items():
    print(f'key: {key}, value: {Value})')







