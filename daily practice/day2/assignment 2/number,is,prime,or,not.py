def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers in the given range are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")