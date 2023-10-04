#!/usr/bin/env python

import random

def main():
  """Start a music genre  guessing game."""
  print("Guess the music genre!") 
 
musicgenre = [
          "pop" ,
          "hip-hop" ,
          "rock" ,
          "r&b" ,
          "remix" ,
          "punkrock" ,
          "classic" ,
          "jazz" ,
          ]
  
x = random.choice(musicgenre)

print("\nAnnyeong yeorobun! Let's play the game together")
print("\n**************************************")
print("\nCan you guess the answer in 3 tries?")
 
guess = None

for count in range(3):

    guess = str(input("\nWhat kind of music genre that i like: "))

    if x == guess:
        print("You guessed {}. Correct!,you're genius".format(guess))
        break
    else:
        print("You guessed {}. Ups!,you've got it wrong.".format(guess))                           
else:
    print("\nTimes up!")          
    print("\nThe correct answer is" , x )