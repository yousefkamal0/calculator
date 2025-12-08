x=(input("Enter a number from 1-100: "))
y=(input("Enter the power you want to raise the number to from 1-5: "))
def power(x, y):
    try:
        base = int(x)
        exponent = int(y)
        if 1 <= base <= 100 and 1 <= exponent <= 100:
            result = base ** exponent
            return f"{base} to the power of {exponent} is {result}"
        else:
            return "numbers must be between 1 and 100"
    except ValueError:
        return "Error dude only add integers"
print(power(x, y))