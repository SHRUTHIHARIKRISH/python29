"""Write a Python program that chooses a random number between 1 and 20. Ask the user to guess the number until they get it right. Give hints “Too high” or “Too low” after each guess. Display how many attempts it took to guess correctly."""
#Ask user to get to choose a  number from 1 to 20
import random
number = random.randint(1, 20)
attempts=0
print("Guess the number from 1 to 20")
while(True):
  guess=int(input(("Enter the guess number:")))
  attempts+=1
  if(guess < number):
    print("Too low")
  elif(guess > number):
    print("Too high")
  else:
       print("Correct!")
       print("The number attempts you took:",attempts)
       break