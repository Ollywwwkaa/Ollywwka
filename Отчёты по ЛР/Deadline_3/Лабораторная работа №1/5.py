def safe_exec(func):
    def wrapper(a, b):
        try:
            result = func(a, b)
            return result
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
            return 0
    return wrapper
@safe_exec
def divide(a, b):
    return a / b
print(f"Результат 1: {divide(10, 2)}")
print(f"Результат 2: {divide(5, 0)}")