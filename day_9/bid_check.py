from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
name = str(input("name: "))
bid = int(input("bid price: "))





dict_bid = {}

def bid_start():
 print(logo)
 name = str(input("name: "))
 bid = int(input("bid price: "))
  
def func(nam,bidd):
 dict_bid[nam]= bidd

func(name,bid)
  
more_bid = input("Any more bids?")

if more_bid == "yes":
  bid_start()
  func(name,bid)
else:
  print("Go Home, Bid is over")
  
  
 


