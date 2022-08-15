def get_input_from_user():
    return input("inter your respons here--->    ")


print('Hello welcome to the program!what is your name')
name_result=get_input_from_user()
print('what is your favourit food?')
food_result=get_input_from_user()
print('whaat is your favourit movies')
movie_result=get_input_from_user() 
print(f"to summarize: your name is {name_result.capitalize()} ,\
your favourit food is {food_result.capitalize()} \
and also your favourit movie is {movie_result.upper()}.")