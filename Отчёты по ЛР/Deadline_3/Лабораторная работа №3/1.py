def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    else:
        return a * power(a, n - 1)
print(power(2, 3))
print(power(5, 0))