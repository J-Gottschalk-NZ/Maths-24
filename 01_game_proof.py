import random

# decorates text
def statement_generator(statement, decoration, style):
  middle = decoration * 3 + " " + statement + " " + decoration * 3
  top_bottom = decoration * len(middle)

  print()

  # adds decoration to top and bottom
  if style == 3:
    print(top_bottom)
    print(middle)
    print(top_bottom)

  else:
    # adds decoration to line only
    print(middle)

  print()

  return ""

# ***** Main Routine Goes here *****

# Sets from http://mbamp.ucsc.edu/files/7915/4393/8152/Maths_24_-_cards.pdf
sets = [
  [2,2,8,6],
  [2,2,4,5],
  [2,4,4,8],
  [8,8,1,7],
  [4,4,8,5],
  [4,6,8,8],
  [8,8,4,4,],
  [6,5,1,1],
  
  
]

valid_symbols = ["+", "-", "*", "/", "(", ")"]

# choose a random set of numbers from the list
numbers = random.choice(sets)

valid_chars = valid_symbols + numbers

# Ask user question
statement_generator("Welcome to the 24 Game", "-", 3)
print()
print("You are given the following numbers:")
for item in numbers:
  print(item, end = "\t")

print()
print("Can you use +, -, * and / to get the number 24? ")

user_ans = input("Type your expression here: ")

for character in user_ans:
  if character not in valid_chars:
    statement_generator("Eek, you are using invalid characters", "#", 3)
    break

user_value = eval(user_ans)

if user_value == 24:
  print("well done!  You got it")
else:
  print("sorry that is not correct")
