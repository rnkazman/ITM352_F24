# Ask the user to enter a number between 1 and 100.  Square the number
# and return the value to the user.
# Name: Rick Kazman
# Date created: 9/4/24

value_entered = input("Please enter an integer between 1 and 100: ")

value_entered_int = int(value_entered)
value_squared = value_entered_int**2
print ("The value squared= ", value_squared)

