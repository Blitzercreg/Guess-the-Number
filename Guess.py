import os
import random
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = random.choice(number_list)

print("I'm thinking of a number between 1 and 10...")

guess = input()

if guess == a:
  print('correct...')
else:
  print('Wrong you piece of garbage!')
  print('It was', a)

restart = input('Would you like to try again stupid? Type y for Yes or n for No\n')
if restart == 'y':
  print('Too bad')
elif restart == 'n':
  print('Loser')
