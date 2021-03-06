import random
import csv
import re
import statistics

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
    info_generator(middle)
    print(top_bottom)

  else:
    # adds decoration to line only
    print(middle)

  # print()

  return ""


# error messages are coloured pink
def error_generator(message):
    error_pink = Color_It(255, 175, 175, message)
    print(error_pink.print_colour())

# information messages are orange    
def info_generator(message):
    info = Color_It(255, 234, 117, message)
    print(info.print_colour())

# success messages are green
def success_generator(message):
    success_message = Color_It(120, 255, 120, message)
    print(success_message.print_colour())

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
    
    # allow exit code of 'xxx'
    if raw_user_ans == "xxx":
        return raw_user_ans
  
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


def yes_no(question):
    
    valid = False
    while not valid:
        response = input(question).lower()
        
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            error_generator("Please enter yes / no\n")
            
def instructions():
    print()
    
    instructions_text = """
    ---- Instructions / Tips ----
    
    You will be given four numbers between 1 and 9.  
    
    Your job is to make the number 24 using all four numbers 
    and the operators +, -,  x and ÷ (/) 

    *** IMPORTANT ***
    Use the '/' symbol for division!!
    
    Expressions are checked using BEDMAS / BEMA which means that 
    you will often need to use brackets.
    
    Your expression should not include an = sign at the end.
    
    If you don't succeed on the first attempt, you should keep 
    trying until you solve the problem.  All of the problems 
    you will get do have a solution.
    
    If you are successful, you will earn virtual swag and 
    bragging rights.  If you get the problem right on the first 
    go you earn more swag than if you need more than one attempt.
    
    Be careful!  If you quit by typing 'xxx' instead of an expression
    you will lose ALL the swag you have earned during your session.
    
    """
    
    info_generator(instructions_text)
    print()
     

# ***** Main Routine Goes here *****


# get sets of numbers from .csv file
# Sets from http://mbamp.ucsc.edu/files/7915/4393/8152/Maths_24_-_cards.pdf
with open('all_sets.csv', newline='') as f:
    reader = csv.reader(f)
    sets = list(reader)

# lists with emoji for feedback...
correct_emoji = ["😊", "😁", "😍", "😇", "😎", "👍", "⭐"]
wrong_emoji = ["😢", "💥", "😭", "👎", "💔"]

# set up swag list
all_swag = "🎈✨👓🏆🧸🍕🍔🍟🥨🍦🧁🍫🍬🍩🍭🍪🍧🍿🍣🍀🍒🌈🦋"
swag_list = []

for item in all_swag:
    swag_list.append(item)
    
problems_solved = 0
problem_attempts = []
quiz_history = []
swag_earned = []

print()
# Heading
statement_generator("Welcome to the 24 Game", "-", 3)
print()

# Ask user if they have played before / show instructions
username = not_blank("Please enter your name: ")
print()

# Game Set up goes here
want_instructions = yes_no("Would you like to read see the instructions? ")

if want_instructions == "yes":
    instructions()

# Questions start here...

keep_going = "yes"
while keep_going == "yes":

    # choose a random set of numbers from the list
    var_numbers = random.choice(sets)
    
    problems_solved += 1
    num_attempts = 0

    # Give Numbers...
    print("\nYour numbers are...")
    
    all_numbers = ""
    for item in var_numbers:
        all_numbers += item
        all_numbers += "\t"
    
    print(all_numbers)

    # Loop for questions...
    status = ""
    while status == "":

    # ask question
        answers = input_checker(var_numbers)
        
        if answers == "xxx":
            swag_earned = []
            keep_going = "no"
            problem_entry = "Problem {}: not attempted <swag cleared>".format(problems_solved)
            quiz_history.append(problem_entry)
            error_generator("\nOh Dear - you quit without solving the problem.")
            error_generator("No swag for you!\n")
            
            break
        
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
            status = "correct"
            var_decoration = random.choice(correct_emoji)
            feedback = "{} well done, you got it {}".format(var_decoration * 3, var_decoration * 3)
            problem_entry = "Problem {} : {} = 24".format(problems_solved, var_raw_ans)
            quiz_history.append(problem_entry)
            success_generator(feedback)

        else:
            calculation = "sorry {} = {}.  Please try again".format(var_raw_ans, var_ans)
            var_decoration = random.choice(wrong_emoji)
            feedback = "{} {} {}".format(var_decoration * 3, calculation, var_decoration * 3)
            error_generator(feedback)
            continue

        # get prize...
        prize_1 = random.choice(swag_list)
        swag_earned.append(prize_1)

        if num_attempts == 1:
            print("\nGreat job - you got it on the first try")
            prize_2 = random.choice(swag_list)
            swag_earned.append(prize_2)
            winnings = "You have won a {} and {}".format(prize_1, prize_2)
        else: 
            print("\nYou solved the problem in {} attempts".format(num_attempts))
            winnings = "You have won a {}".format(prize_1)
        
        print()
        success_generator(winnings)
        print()
        
        # update attempts list for stats
        problem_attempts.append(num_attempts)
        
        
    keep_going = yes_no("Would you like to attempt another problem? ")
    
print()    

statement_generator("{} - Summary Information".format(username), "-", 3)

print()

if problems_solved > 1:
    
    info_generator("Statistics...")
    
    best = min(problem_attempts)
    worst = max(problem_attempts)
    average = statistics.mean(problem_attempts)


    print("Games Played: {}".format(problems_solved))
    print("Best Score: {}".format(best))
    
    if best != worst:
        print("Worst Score: {}".format(worst))
    
    print("Average Score: {}".format(average))


    statement_generator("Game History", "-", 3)
    for item in quiz_history:
        print(item)
        
else:
    print("We don't have any statistics to share as you completed less than two problems.")

# Swag goes here
statement_generator("Swag!!", "*", 3)
print()

if len(swag_earned) > 0:
    
    info_generator("Here is your swag...")
    
    for item in swag_earned:
        print(item, end=" ")
        
else:
    info_generator("""
Sorry - no swag here.  

It looks like you quit without solving one of the 
problems and the swag monster came and took away 
all your swag.

          """)
    
        


print()
print()
print("Thanks for Playing")
print()