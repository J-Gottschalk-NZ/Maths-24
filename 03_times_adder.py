import re

# adds * sign between numbers and brackets

def times_adder(expression):
  # RegEx from here...
  # https://stackoverflow.com/questions/53228036/insert-multiplication-sign-between-parenthesis
  return re.sub('(?<=\d|\))(\()', '*(', expression)

#  **** Main Routine goes here ****

test_strings = [
  "3(2 + 1)",
  "(2+2) - 3(4+1)",
  "2(1+2) + 3(4-1)",
  "(5)(2) + 3(2)"
]

for item in test_strings:
  fixed = times_adder(item)
  user_ans = eval(fixed)
  print("{} = {}".format(item, user_ans))
  # print(fixed)