operator = str(input("Enter you operator (+ - * /):"))
num1 = float(input("Enter you number1:"))
num2 = float(input("Enter you number2:"))
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("operator you incorect")