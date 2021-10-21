def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def multi(number1, number2):
    return number1 * number2

def div(number1, number2):
    if number2 == 0:
        return None
    else:
        return number1 / number2

def process(number1, number2, operation):
    if operation == '+':
        return add(number1, number2)
    elif operation == '-':
        return sub(number1, number2)
    elif operation == '*':
        return multi(number1, number2)
    elif operation == '/':
        return div(number1, number2)
    else:
        return "This operation isn't supported!"
