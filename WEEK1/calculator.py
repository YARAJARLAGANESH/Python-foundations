def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")

        print("Result:", result)

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")

    except ZeroDivisionError as e:
        print(e)

    except Exception as e:
        print("Unexpected error:", e)


calculator()