# Ask the user to enter a whole number between 1 and 100. Square the number
# and return the value to the user.
# Name: Rick Kazman
# Date created: 9/2/25

# Prompt the user for input
value_entered = input("Please enter a whole number between 1 and 100: ")

# Convert the input to an integer
value_entered_int = int(value_entered)

# Square the number
value_squared = value_entered_int ** 2

# Print the result
print(f"You entered {value_entered_int}. The square of {value_entered_int} is {value_squared}.")