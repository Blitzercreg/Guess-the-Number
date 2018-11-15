# This is a number guessing game made for Python 3
# Version 1.05

import random

def answer():
  restart = input('\nWould you like to try again stupid? Type Y for Yes or N for No\n')
  if restart == 'y':
    print('\n')
    start()
  elif restart == 'n':
    print('Loser')
    quit()
  elif restart != 'n' or 'y':
    print('Thats not even an option I gave you!')
    answer()

def start():
  number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  a = random.choice(number_list)

  print("I'm thinking of a number between 1 and 10...")

  guess = input()

  try:
    if int(guess) == a:
      print('NO! Haha you dummy, you said it was', guess, 'when really it was...\n', a)
    elif int(guess) != a:
      print('Wrong you piece of garbage!')
      print('It was', a)
  except ValueError:
      print('That is not even a number you disgusting hippopotamus!')
  answer()

def banner(message, border='~'):
  line = border * len(message)
  print(line)
  print(message)
  print(line)
  print('\n')

banner('Welcome to the Guessing Game!')
start()
