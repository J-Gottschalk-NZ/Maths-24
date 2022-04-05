import re

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

  print()

  return ""


def input_checker(numbers):


  valid_symbols = ["+", "-", "*", "/", "(", ")", " "]
  
  # change numbers to string
  string_numbers = []
  for item in numbers:
    string_numbers.append(str(item))
  
  # add numbers to list
  valid_chars = valid_symbols + string_numbers

  valid = False
  while not valid:
    numbers_used = []

    print("Your numbers are...")
    for item in numbers:
      print(item, end = "\t")

    print()
    
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

# Sets from http://mbamp.ucsc.edu/files/7915/4393/8152/Maths_24_-_cards.pdf


var_numbers = [2,3,4,5]
answers = input_checker(var_numbers)
print(answers[0])
print(answers[1])