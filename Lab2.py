# Lab 2, calculator
# Alden Smallwood

num1 = int(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = int(input("Enter a number: "))

dictionary = {  # a dictionary that pairs operators and their corresponding math statements
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2,
    "%": num1 % num2,
    "^": num1 ** num2
}

if operator in dictionary:  # if the operator the user entered is in the dictionary (a valid operator),
    # execute the corresponding math statement in dictionary and print
    print(num1, operator, num2, " = ", dictionary[operator])
else:  # if the operator is not in the dictionary, print an error statement
    print("Error, ", operator, " is not a valid operator")

