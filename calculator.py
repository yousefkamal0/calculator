def divide():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b == 0:
        print("Error: you can't divide by zero")
        return

    print("Result:", a / b)

divide()
