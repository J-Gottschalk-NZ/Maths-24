def input_checker(string_numbers, var_all_numbers):

  valid_symbols = ["+", "-", "*", "/", "(", ")", " "]
   
  # add numbers to list
  valid_chars = valid_symbols + string_numbers
  
  valid = False
  while not valid:
    numbers_used = []
    
    # assume no errors at start
    error = ""

    print("\n")
    
    print("Your numbers are:")
    print(var_all_numbers)
    raw_user_ans = input("Type your expression here: ").lower()
    
    # allow exit code of 'xxx'
    if raw_user_ans == "xxx":
        return raw_user_ans
  
    # add multiply signs between brackets if needed
    user_ans = raw_user_ans
    
    for character in user_ans:
      
      if character not in valid_chars:
        
        error = "yes"
        
        print("Oops - the '{}' character  is not allowed in your expression for this problem".format(character))
        print()
        
        break
      else:
        if character in string_numbers:
          numbers_used.append(character)
    
    # sort numbers used
    numbers_used.sort()

    # sort numbers in question
    string_numbers.sort()

    
    if numbers_used == string_numbers:
        print("you have used all the numbers")
    else:
        print("you have not used all the given numbers once only")
          
    if error != "":
      pass
    
    # elif len(numbers_used) != 4:
    #   print("You need to use each number once, you have used {} numbers".format(len(numbers_used)))
  
    else:
      return [raw_user_ans, user_ans]


var_numbers = ['3', '4', '5', '6']

all_numbers = ""
for item in var_numbers:
    all_numbers += item
    all_numbers += "\t"
    
answers = input_checker(var_numbers, all_numbers)

print(answers)