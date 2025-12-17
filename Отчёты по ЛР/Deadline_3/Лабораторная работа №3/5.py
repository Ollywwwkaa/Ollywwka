import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n-1, b, a+b)
n = 35
start = time.time()
print(f"Fibonacci({n}) = {fibonacci(n)}")
print(f"Time taken (Naive): {time.time() - start:.6f} seconds")
start = time.time()
print(f"Tail Fibonacci({n}) = {tail_fibonacci(n)}")
print(f"Time taken (Tail): {time.time() - start:.6f} seconds")