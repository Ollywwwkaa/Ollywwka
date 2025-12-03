def logger(fun):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {fun} с аргументами - {args} {kwargs}")
        res = fun(*args, **kwargs)
        print(f"Результат = {res}")
        return res 
    return wrapper
@logger
def add(a,b):
    return a + b
add(5,10)