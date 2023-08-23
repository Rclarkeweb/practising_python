# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2
    
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = int(input("Enter your first number: "))

    for operator in operations:
        print(operator)
    
    user_exit = True
    while user_exit:
    
        chosen_operator = input("Enter an operator: ")

        num2 = int(input("Enter another number: "))

        calculate = operations[chosen_operator]

        answer = calculate(num1, num2)

        print(f"{num1} {chosen_operator} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer} : ") == "y":
            num1 = answer
        else:
            user_exit = False
            calculator()
            
calculator()
