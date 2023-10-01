import random
import time
correct_number= random.randint(1,100)
print("Welcome to the guessing game")
time.sleep(2)
print("Picking the number: ")
time.sleep(2)
guess= int(input("What's your guess? "))
guess_number=1
while (guess!=correct_number):
  guess_number+=1
  if (guess < correct_number):
    guess=int(input("You are way down, come up! what's your new guess ?"))
    time.sleep(1)
  else:
    guess=int(input("You are aiming too high, lower your level!! what's your new guess? "))
time.sleep(1)
print(f"Finally, after {guess_number} attempts, you have guessed it correctly! The number is {guess}")