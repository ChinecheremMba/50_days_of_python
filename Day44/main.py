def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

while True:
    try:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        user_input = input(": ")

        if user_input == "quit":
            break

        if user_input not in ("add", "subtract", "multiply", "divide"):
            raise NameError("Invalid input. Please enter a valid operation.")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            result = add(num1, num2)
        elif user_input == "subtract":
            result = subtract(num1, num2)
        elif user_input == "multiply":
            result = multiply(num1, num2)
        elif user_input == "divide":
            result = divide(num1, num2)

        print("Result:", result)

    except ZeroDivisionError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except NameError as e:
        print("Error:", e)
