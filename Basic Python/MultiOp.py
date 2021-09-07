# Read user input and store as an integer

firstNumber = int(input("What's the first number?"))
secondNumber = int(input("What's the second number?"))

# Perform maths and store as variable

sum = firstNumber + secondNumber
sub = firstNumber - secondNumber
mul = firstNumber * secondNumber

# Print equation and sum

print(firstNumber, '+', secondNumber, '=', sum)
print(firstNumber, '-', secondNumber, '=', sub)
print(firstNumber, '*', secondNumber, '=', mul)

# Calculate / print division and sum if user stored numbers are greater than zero

if(firstNumber and secondNumber > 0):
    div = firstNumber / secondNumber
    print(firstNumber, '/', secondNumber, '=', div)
else:
    print("Please enter a number greater than zero for division!")
