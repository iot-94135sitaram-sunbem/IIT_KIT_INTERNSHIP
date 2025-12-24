
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

num = 5
print("Factorial of", num, "is:", factorial(num))

base = 2
exp = 3
print("Power:", base, "^", exp, "=", power(base, exp))