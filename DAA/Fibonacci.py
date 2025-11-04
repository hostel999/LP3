# Recursive Fibonacci
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
n = 10
print("Recursive Fibonacci of", n, ":", fibonacci_recursive(n))

# Non-Recursive, Iterative Fibonacci
def fibonacci_iterative(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        print("Iterating:", a)
        a, b = b, a + b
    return b 

# Test
n = 10
print("Iterative Fibonacci of", n, ":", fibonacci_iterative(n))
