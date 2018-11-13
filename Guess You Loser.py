# This is a number guessing game made for Python 3

import os
import random
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = random.choice(number_list)

print("I'm thinking of a number between 1 and 10...")

guess = input()

if int(guess) == a:
  print('NO! Haha you dummy, you said it was', guess, 'when really it was...\n', a)
elif int(guess) != a:
  print('Wrong you piece of garbage!')
  print('It was', a)

while True:
  try:
    restart = input('Would you like to try again stupid? Type Y for Yes or N for No\n')
    if restart == 'y':
      print('Too bad')
      break
    elif restart == 'n':
      print('Loser')
      break
    elif restart != 'n' or 'y':
      print('Thats not even an option I gave you!')
  except:
    print('e') # I am not sure how to get the 'except' function to go through