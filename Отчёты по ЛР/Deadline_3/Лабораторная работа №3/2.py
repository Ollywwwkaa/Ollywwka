def sum_digits(num):
    num = abs(num)
    if num < 10:
        return num
    else:
        return (num % 10) + sum_digits(num // 10)
print(sum_digits(12345))
print(sum_digits(987))
print(sum_digits(0))
print(sum_digits(-4))