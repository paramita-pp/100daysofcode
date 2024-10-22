from art import logo

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply, divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as values: Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculation. Multiply 4 * 8 use
# print(operations["/"](4,2))

# Program asks the user type the first number
def calculator():
    print(logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        math_operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        output = operations[math_operator](num1, num2)
        print(f"{num1} {math_operator} {num2} = {output}")



        choice =input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
        if choice == 'y':
            num1 = output
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()


calculator()
