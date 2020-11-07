import random

# colors = ['red', 'blue', 'green']

# random_color = colors[random.randint(0,len(colors)-1)]

# guess = input('What color?')

# while True:
#     if (guess == random_color.lower()):
#         input('Correct!')
#         keep_playing = input('Keep playing?')
#         if (keep_playing == 'yes'):
#             random_color = colors[random.randint(0,2)]
#             continue
#         else:
#             break
#     else:
#         guess = input('What color?')

# -----------------------------------------------------------

# import random

# people = []

# for x in range(0,6):
#     person = input('Name please?')
#     people.append(person)

# print(f'Winner is: {people[random.randint(0,5)]}')

# -----------------------------------------------------------
 
# height = float( input('What is your height?') )
# weight = float( input('What is your weight?') )

# bmi = (weight / (height * height)) * 703

# print(f'Your BMI is: {bmi}')

# if(bmi <= 18.5):
#     print('Underweight')
# elif(bmi > 18.5 and bmi <= 24.9):
#     print('Normal weight')
# elif(bmi > 24.9 and bmi <= 29.9):
#     print('Overweight')
# else:
#     print('Obesity')

# -----------------------------------------------------------

# my_age = 42
# user_age = int( input('What is your age?') ) 

# if(my_age < user_age):
#     print('You are older than me.')
# elif(my_age > user_age):
#     print('I am older than you.')
# else:
#     print('We are the same age.')

# -----------------------------------------------------------

# person = {
#     "name": "Tony",
#     "gender": "male",
#     "age": 42,
#     "address": "7465 Salizar St, San Diego, CA 92111",
#     "phone": "850-529-9293"
# }

# key = input('What do you want to know about SnakePlisskinA1?').lower()

# result = person.get(key, 'Sorry, you can not enter.')

# print(f'{result}')

# -----------------------------------------------------------

# people = ['Mary', 'Jack', 'Barnes', 'Berry']

# user = input( 'What is your name?' )

# people.append(user)

# print(people)

# -----------------------------------------------------------

# months = ('January', 'Febuary', 'March', 'April', 'May', 'June')

# birthdate = input( 'What is your birthdate?' )
# index = int(birthdate[3:5]) - 1
# bd_month = months[index]

# print( f'You were born in {bd_month}' )

# -----------------------------------------------------------

# import math

# radius = float( input( 'Radius?' ) )

# area = round( math.pi * ( radius ** 2 ), 2 )
# circumference = round( 2 * math.pi * radius, 2 )

# print( f'Area = {area}' )
# print( f'Circumference = {circumference}' )