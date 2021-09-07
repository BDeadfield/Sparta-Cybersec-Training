# Import module to perform calculations

from calcPackage import calcModule

# Read user input for numbers

def userInput():
    x = int(input("What's the first number?"))
    y = int(input("What's the second number?"))
    return x, y

# Format results for printing to user

def printResult (number1, number2, operation, result):
    equation = f"{firstNumber} {operation} {secondNumber} = {result}"
    print(equation)

# Iterate through and print results including formatting (unless one of the numbers is zero)

for index in range (0, 5):

    firstNumber, secondNumber = userInput()

    sum = calcModule.addition(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '+', sum)

    sub = calcModule.subtraction(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '-', sub)

    multi = calcModule.multiplication(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '*', multi)

    div = calcModule.division(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '/', div)
