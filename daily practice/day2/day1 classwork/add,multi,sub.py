num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid choice")