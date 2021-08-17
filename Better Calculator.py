
num1 = float(input("Enter first number: "))
op = (input("Enter + or - or / or * : "))
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid. Please use + or - or / or *")
