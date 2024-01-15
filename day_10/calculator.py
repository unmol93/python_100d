from art import logo

def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def mul(a,b):
  return a * b

def div(a,b):
  return a / b

def start():
  #clear()
  print(logo)

a = int(input("What is the first number?: "))
print("+ ")
print("- ")
print("* ")
print("/ ")
operator = str(input("Pick an operator: "))
b = int(input("What is the next number?: "))

def check(g,h):
 if operator == "+" :
   num = add(g,h)
   print(num)
 elif operator == "-" :
  num = sub(g,h)
  print(num)
 elif operator == "*" :
  num = mul(g,h)
  print(num)
 elif operator == "/":
  num = div(g,h)
  print(num)
 x = str(input(f"Type y to continue calculate with {num}, or type 'n' to start a new cal "))
 return num, x

num, z = check(a, b)

while z.lower() == "y":
    a = num
    b = int(input("What is the next number?: "))
    operator = str(input("Pick an operator: "))
    result, z = check(a, b)

print("Game over")
  





