user_input = input("Do you want to use the calculator? Type Y to continue: ")
while user_input == "Y":
    try:
        num1 = float(input("Enter a number: "))
        operator = input(("Enter an operator, pick from + - * / : "))
        num2 = float(input("Enter a second number: "))
        if operator == "+":
            print(num1, operator, num2, "=", (num1+num2))
        elif operator == "-":
            print(num1, operator, num2, "=", (num1-num2))
        elif operator == "*":
            print(num1, operator, num2, "=", (num1*num2))
        elif operator == "/":
            print(num1, operator, num2, "=", (num1/num2))
        else:
            print("Please enter a valid operator")
    except ZeroDivisionError:
        print("Cannot divide by zero, please try again")
    except ValueError:
        print("Please enter a valid number to continue")
    user_input = input("Do you want to continue using the calculator? Type Y to continue or N to stop: ")
else:
    print("Calculator stopped. Thanks for using the calculator, goodbye!")