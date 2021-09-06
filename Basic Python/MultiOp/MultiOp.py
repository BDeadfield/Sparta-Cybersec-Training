firstNumber = int(input("What's the first number?"))
secondNumber = int(input("What's the second number?"))

sum = firstNumber + secondNumber
sub = firstNumber - secondNumber
mul = firstNumber * secondNumber

print(firstNumber, '+', secondNumber, '=', sum)
print(firstNumber, '-', secondNumber, '=', sub)
print(firstNumber, '*', secondNumber, '=', mul)

if(firstNumber and secondNumber > 0):
    div = firstNumber / secondNumber
    print(firstNumber, '/', secondNumber, '=', div)
else:
    print("Please enter a number greater than zero for division!")
