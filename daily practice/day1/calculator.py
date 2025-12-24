print("Enter first number:")
num1 = float(input())
print("Enter second number:")
num2 = float(input())
print("Select operation (+, -, *, /):")
operation = input()
if operation == '+':
    result = num1 + num2
    print("The result is: " + str(result))
elif operation == '-':
    result = num1 - num2
    print("The result is: " + str(result))
elif operation == '*':
    result = num1 * num2
    print("The result is: " + str(result))
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result is: " + str(result))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")