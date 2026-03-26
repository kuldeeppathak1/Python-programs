n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\n")
############ Using recursion (interview favorite)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")