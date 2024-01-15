from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
name = str(input("name: "))
bid = int(input("bid price: "))





dict_bid = {}

def bid_start():
 clear()
 print(logo)
 

def func(nam,bidd):
 dict_bid[nam]= bidd

func(name,bid)

more_bid = input("Any more bids?")

while more_bid == "yes":
  bid_start()
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: "))
  func(name,bid)
  print(f"Bids so far: {dict_bid}")
  more_bid = input("Any more bids?")



# Calculate and display the winner
winner_name = max(dict_bid, key=dict_bid.get)
winning_bid = dict_bid[winner_name]

print(f"\nThe winner is {winner_name} with a bid of {winning_bid}.")









