# Ask the user to enter a floating point number between 1 and 100.  Square the number
# and return the value to the user.
# Name: Rick Kazman
# Date created: 9/6/24

value_entered = input("Please enter an floating point number between 1 and 100: ")

value_entered = float(value_entered)
value_squared = value_entered**2
print ("The value squared= ", value_squared)
