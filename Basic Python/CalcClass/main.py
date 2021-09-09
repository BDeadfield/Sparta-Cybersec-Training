import calculator

for index in range(0, 5):
    number1 = int(input("Please enter the first number:  "))
    number2 = int(input("Please enter the second number:  "))

    calculatorObject = calculator.CalculatorClass(number1, number2)

    sum = calculatorObject.add()
    print ("Addition: ", sum)
    print(f"Total Operationns = {calculator.CalculatorClass.op_count}")

    sub = calculatorObject.subtract()
    print("Subtraction: ", sub)
    print(f"Total Operationns = {calculator.CalculatorClass.op_count}")

    multi = calculatorObject.multiply()
    print("Multiplication: ", multi)
    print(f"Total Operationns = {calculator.CalculatorClass.op_count}")

    div = calculatorObject.divide()
    print("Divide: ", div)
    print(f"Total Operationns = {calculator.CalculatorClass.op_count}")
