def to_binary(n):
    binary = ""
    if n == 0:
        binary = "0"
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2   
    print("Binary:", binary)
num = int(input("Enter a number: "))
to_binary(num)
