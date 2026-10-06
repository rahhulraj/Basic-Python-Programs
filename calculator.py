num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")
match operator:
    case '+':
        print("SUM:", num1 + num2)

    case '-':
        print("SUB:", num1 - num2)

    case '*':
        print("MULTIPLE:", num1 * num2)

    case '/':
        if num2 != 0:
            print("DIVISION:", num1 / num2)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator!")