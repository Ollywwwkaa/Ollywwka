def repeat (n):
    def decorator (fun):
        def wrapper(*args, **kwargs):
            for i in range(n):
                fun (*args, *kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet (name):
    print(f"Привет, {name}!")
greet("Вася")