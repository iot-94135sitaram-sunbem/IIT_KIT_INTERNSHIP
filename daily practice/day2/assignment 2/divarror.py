num1 = float(input("Enter dividend: "))
num2 = float(input("Enter divisor: "))
if(num2!=0):
    print(f"{num1} / {num2} = {num1 / num2}")
elif(num2==0):
    print(f"division error")