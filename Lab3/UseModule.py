# Program to test the use of the HandyMath library
import HandyMath as HM

number1 = input("Enter first value: ")
number2 = float(input("Enter second value: "))
number1 = float(number1)


mid = HM.midpoint(number1, number2)
print("The midpoint is: ", mid)
