number1 = int(input("Enter the first number: "))
print("You entered:", number1)

number2 = int(input("Enter the second number: "))
print("You entered:", number1, "and", number2)

number2 = int(input("Enter the second number: "))
print("You have:", number1, "and", number2)

operation = input("Enter the operation (+, -, *, /): ")
print("You want to do:", number1, operation, number2)

if operation == "+":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

elif operation == "-":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == "*":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "/":
    result = number1 / number2
    print(f"{number1} / {number2} = {result}")
else:
    print("Invalid operation!") 
