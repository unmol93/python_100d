from art import logo
import random

ran_num = random.randint(1, 100)
print(logo)
print("Welcome to the guessing game")
print("I am thinking of a number between 1 to 100")
x = input("Choose a difficulty. Type Easy or Hard? ")
if x == "Easy":
  easy = 10
  while 0 < easy <= 10:
    print(f"You have {easy} attempts left.")

    a = int(input("Make a guess "))
    if a == ran_num:
      print("You Won")
      break
    elif a > ran_num:
      print("Too high")
      easy = easy -1
    elif a < ran_num:
     print("Too low")
     easy = easy -1

  if easy == 0:
    print(f"You loose. The number was {ran_num} ")
elif x == "Hard":
  hard = 5
  while 0 < hard <= 5:
    print(f"You have {hard} attempts left.")
    a = int(input("Make a guess "))
    if a == ran_num:
      print("You Won")
      break
    elif a > ran_num:
      print("Too high")
      hard = hard -1
    elif a < ran_num:
     print("Too low")
     hard = hard -1
  if hard == 0:
    print(f"You loose. The number was {ran_num} ")

