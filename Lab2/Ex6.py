# Ask the user to enter their weight in pounds.  Convert to kilos and output

weight_in_pounds = input("Please enter your weight in pounds: ")

weight_in_pounds = float(weight_in_pounds)
POUNDS_TO_KILOS = 0.453592

weight_in_kilos = weight_in_pounds * POUNDS_TO_KILOS

print("You weigh ", round(weight_in_kilos,1), " kilos")
