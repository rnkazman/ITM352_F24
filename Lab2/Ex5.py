# Ask the user to enter an arbitrary sentence.  Calculate the length of that
# string and return that value.

sentence = input("Enter a sentence: ")

stringLength = len(sentence)
outputString = "You entered \"" + sentence + "\". It has length " + str(stringLength)
print(outputString)
