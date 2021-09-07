# Read user input for numbers

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

def printResult (number1, number2, operation, result):
    text = f"{firstNumber} {operation} {secondNumber} = {result}"
    print(text)

# Iterate through and print results including formatting (unless one of the numbers is zero)

for index in range (0, 5):

    firstNumber, secondNumber = userInput()

    sum = addition(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '+', sum)

    sub = addition(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '+', sub)

    multi = addition(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '+', multi)

    div = division(firstNumber, secondNumber)
    printResult(firstNumber, secondNumber, '/', div)
