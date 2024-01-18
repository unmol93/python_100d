from art import logo
from art import vs
import random
from game_data import data

right_answer = True
score = 0
while right_answer == True:
  print(logo)
  print(right_answer)
  num1, num2 = random.randint(0, len(data)), random.randint(0, len(data))
  dict1 = data[num1]
  dict2 = data[num2]
  print(f"Compare A: {dict1['name']}, a {dict1['description']}, from {dict1['country']}")
  a_followers = int(dict1['follower_count'])
  print(vs)
  print(f"Against B: {dict2['name']}, a {dict2['description']}, from {dict2['country']}")
  b_followers = int(dict2['follower_count'])
  if a_followers > b_followers:
    answer = 'A'
  else:
    answer = 'B'
  x = str(input("who has more followers? 'A' or 'B' "))
  if x == answer:
    right_answer = True
    score = score + 1
    print(f"Your current score is: {score}")
    
  else:
    right_answer = False

print(f"You loose! final score is : {score}")
  








