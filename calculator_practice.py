user_input = input("Do you want to use the calculator? Type Y to continue: ")
while user_input == "Y":
    num1 = int(input("Enter a number: "))
    operator = input(("Enter an operator, pick from + - * / : "))
    num2 = int(input("Enter a second number: "))
    if operator == "+":
        print(num1, operator, num2, "=", (num1+num2))
    elif operator == "-":
        print(num1, operator, num2, "=", (num1-num2))
    elif operator == "*":
        print(num1, operator, num2, "=", (num1*num2))
    elif  operator == "/":
        print(num1, operator, num2, "=", (num1/num2))
    user_input = input("Do you want to continue to use the calculator? Type Y to continue or N to stop: ")
else:
    print("Calculator stopped.")
