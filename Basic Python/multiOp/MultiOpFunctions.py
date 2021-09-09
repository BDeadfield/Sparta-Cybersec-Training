import json

# Read user input and store as integer

def userInput():
    x = int(input("What's the first number?"))
    y = int(input("What's the second number?"))
    return x, y

# Perform mathematics for sum totals

def addition(firstNumber, secondNumber):
    total = firstNumber + secondNumber
    return total

def subtraction(firstNumber, secondNumber):
    total = firstNumber - secondNumber
    return total

def multiplication(firstNumber, secondNumber):
    total = firstNumber * secondNumber
    return total

def division(firstNumber, secondNumber):
    try:
        total = firstNumber / secondNumber
    except ZeroDivisionError:
        print("\nYou can't divide by 0!\n")
        return None
    except:
        print("Unknown error!")
        return None
    return total

# Format results for printing to user

def result (number1, operation, number2, result):
    equation = f"{firstNumber} {operation} {secondNumber} = {result}"
    return equation

# Create counter for loops

counter = 0

# Loop five times taking users input for two numbers, totalling results from four different operations and formatting them as an equation, then saving this format as a dictionary in a json file

for index in range (counter, 5):

    counter += 1

    firstNumber, secondNumber = userInput()

    sumResult = addition(firstNumber, secondNumber)
    subResult = subtraction(firstNumber, secondNumber)
    multiResult = multiplication(firstNumber, secondNumber)
    divResult = division(firstNumber, secondNumber)

    sum = result(firstNumber, '+', secondNumber, sumResult)
    sub = result(firstNumber, '-', secondNumber, subResult)
    multi = result(firstNumber, '*', secondNumber, multiResult)
    div = result(firstNumber, '/', secondNumber, divResult)

    equations =  {
        'Addition': sum,
        'Subtraction': sub,
        'Multiplication': multi,
        'Division': div,
    }

    mainDict = {
        counter: equations,
    }

    print(mainDict)

    with open('results.json', 'a+') as file:
        json.dump(mainDict, file, indent = 4)
