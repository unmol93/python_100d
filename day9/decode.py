alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
##["foo", "bar", "baz"].index("bar")

def encrypt(text,shift):
  text_list = []
  new_list = []
  final_list = []
  for i in text:
    text_list.append(i)
  if direction == "encode":
   for alph in text_list:
     if alph in alphabet:
      position = alphabet.index(alph) + shift
      new_list.append(position)
   for a in new_list:
     wordd = alphabet[a]
     final_list.append(wordd)
  else:
    for alph in text_list:
       if alph in alphabet:
        position = alphabet.index(alph) - shift
        new_list.append(position)
    for a in new_list:
       wordd = alphabet[a]
       final_list.append(wordd)
    
  word = ""
  for b in final_list:
    fin_word = b
    word = word + fin_word
    

  
  print(word)

  
 
encrypt(text,shift)
 


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
