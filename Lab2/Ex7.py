# Ask the user to input a temperature in degrees Fahrenheit.
# Convert that temperature to Celsius and output it.

degreesF = input("Enter a temperature in Fahrenheit: ")

degreesC = (float(degreesF) - 32) * (5/9)

print("This converts to ", degreesC, "Celsius")