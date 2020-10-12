def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")

def is_positive(number):
  if number > 0:
    return True

def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative