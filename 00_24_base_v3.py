import random
import csv
import re

# Class for coloured text, used for error generator 
# (and other text colouring functions)
class Color_It():
    
    def __init__(self, red, green, blue, text):
        self.red = red
        self.green = green
        self.blue = blue
        self.text = text

    def get_color_escape(self, red, green, blue):
        return '\033[{};2;{};{};{}m'.format(38, red, green, blue)
    
    def print_colour(self):
        # the bit at the end resets the colour back to normal
        all_coloured = self.get_color_escape(self.red, self.green, self.blue) + self.text + '\033[0;0m'
        return all_coloured

# checks that input is not blank...
def not_blank(question):
  
  valid = False
  while not valid:
    response = input(question)
    
    if response != "":
      return response
    else:
      error_generator("Sorry - your name can't be blank")
      print()
    
    print()


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


def error_generator(message):
    error_pink = Color_It(255, 175, 175, message)
    print(error_pink.print_colour())

# checks expression is valid
def input_checker(string_numbers):

  valid_symbols = ["+", "-", "*", "/", "(", ")", " "]
   
  # add numbers to list
  valid_chars = valid_symbols + string_numbers
  
  valid = False
  while not valid:
    numbers_used = []
    
    # assume no errors at start
    error = ""

    print("\n")
    
    raw_user_ans = input("Type your expression here: ").lower()
  
    # add multiply signs between brackets if needed
    user_ans = times_adder(raw_user_ans)
    
    for character in user_ans:
      
      if character not in valid_chars:
        
        error = "yes"
        
        error_generator("Oops - the '{}' character  is not allowed in your expression for this problem".format(character))
        print()
        
        break
      else:
        if character in string_numbers:
          numbers_used.append(character)
          
    if error != "":
      pass
    
    elif len(numbers_used) != 4:
      error_generator("You need to use each number once, you have used {} numbers".format(len(numbers_used)))
  
    else:
      return [raw_user_ans, user_ans]

# ***** Main Routine Goes here *****


# get sets of numbers from .csv file
# Sets from http://mbamp.ucsc.edu/files/7915/4393/8152/Maths_24_-_cards.pdf
with open('all_sets.csv', newline='') as f:
    reader = csv.reader(f)
    sets = list(reader)

# lists with emoji for feedback...
correct_emoji = ["😊", "😁", "😍", "😇", "😎", "👍", "⭐"]
wrong_emoji = ["😢", "💥", "😭", "👎", "💔"]

# Heading
statement_generator("Welcome to the 24 Game", "-", 3)
print()
  
# Ask user if they have played before / show instructions
username = not_blank("Please enter your name: ")

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
    # out put error message (pink text)
    error_generator("Oops something went wrong.  You might have unclosed brackets / operators that are not separated by numbers")
    
    print("")
    continue

  num_attempts += 1

  # Check answer
  if var_ans == 24:
    feedback = "well done, you got it"
    status = "correct"
    var_decoration = random.choice(correct_emoji)

  else:
    feedback = "sorry {} = {}.  Please try again".format(var_raw_ans, var_ans)
    var_decoration = random.choice(wrong_emoji)

  statement_generator(feedback, var_decoration, 1)

if num_attempts == 1:
  print("\nGreat job - you got it on the first try")
else: 
  print("\nYou solved the problem in {} attempts".format(num_attempts))