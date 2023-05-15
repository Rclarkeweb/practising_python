# Calculator

num1 = int(input("Type your first number: "))
operator = input("Choose between: + / - * : ")
num2 = int(input("Type your next number: "))
print(num1, operator, num2)

if operator == '+':
    answer = num1 + num2
elif operator == '/':
    answer = num1 // num2
elif operator == '-':
    answer = num1 - num2
elif operator == '*':
    answer = num1 * num2
else:
    print('Sorry that calculation cant be performed')
    exit()
    
print("= ", answer)
