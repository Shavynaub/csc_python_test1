opp = input("Enter 1 of the following operations: + - * /")
num1 = float(input("Enter your first number"))
num2 = float(input("Enter your 2nd Number"))

if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(num1-num2)
elif opp == "*":
    print(num1 * num2)
elif opp == "/":
    print(num1/num2)
else:
    print("Invalid operation")