import random
import csv
import re
from symtable import Symbol

# adds * sign between numbers and brackets
# replaces x with *
def times_adder(expression):

    # replace 'x' and '×' with *
  expression = expression.replace('x', '*' )
  expression = expression.replace('×', '*')
  
  # RegEx from here...
  # https://stackoverflow.com/questions/53228036/insert-multiplication-sign-between-parenthesis
  return re.sub('(?<=\d|\))(\()', '*(', expression)


# Statement decorator
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

  # print()

  return ""



def input_checker(string_numbers):

  valid_symbols = ["+", "-", "*", "/", "(", ")", " "]
   
  # add numbers to list
  valid_chars = valid_symbols + string_numbers

  valid = False
  while not valid:
    numbers_used = []

    print("\n")
    
    raw_user_ans = input("Type your expression here: ").lower()
  
    # add multiply signs between brackets if needed
    user_ans = times_adder(raw_user_ans)
    
    for character in user_ans:
      
      if character not in valid_chars:
        statement_generator("Eek, you are using invalid characters", "#", 3)
        break
      else:
        if character in string_numbers:
          numbers_used.append(character)
    
    if len(numbers_used) != 4:
      print("You need to use each number once, you have used {} numbers".format(len(numbers_used)))
  
    else:
      return [raw_user_ans, user_ans]

# ***** Main Routine Goes here *****


# get sets of numbers from .csv file
# Sets from http://mbamp.ucsc.edu/files/7915/4393/8152/Maths_24_-_cards.pdf
with open('all_sets.csv', newline='') as f:
    reader = csv.reader(f)
    sets = list(reader)

# Heading
statement_generator("Welcome to the 24 Game", "-", 3)

  
# Ask user if they have played before / show instructions

# choose a random set of numbers from the list
var_numbers = random.choice(sets)

num_attempts = 0

# Give Numbers...
print("\nYour numbers are...")
for item in var_numbers:
  print(item, end = "\t")

# Loop for questions...
status = ""
while status == "":

  # ask question
  answers = input_checker(var_numbers)
  
  var_raw_ans = answers[0]
  
  try:
    var_ans = eval(answers[1])
    
  except SyntaxError:
    print("Oops something went wrong.  You might have unclosed brackets / operators that are not separated by numbers")
    continue

  num_attempts += 1

  # Check answer
  if var_ans == 24:
    feedback = "well done, you got it"
    status = "correct"
    var_decoration = "😊"

  else:
    feedback = "sorry {} = {}.  Please try again".format(var_raw_ans, var_ans)
    var_decoration = "🍕"

  statement_generator(feedback, var_decoration, 1)

if num_attempts == 1:
  print("\nGreat job - you got it on the first try")
else: 
  print("\nYou solved the problem in {} attempts".format(num_attempts))