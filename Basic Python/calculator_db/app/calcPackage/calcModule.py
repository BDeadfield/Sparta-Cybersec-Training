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
        print("Unkown error!")
        return None
    return total
