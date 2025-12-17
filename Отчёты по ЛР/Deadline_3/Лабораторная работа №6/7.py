class Person:
    def __init__(self, name, age):
        super().__setattr__('name', name)
        super().__setattr__('age', age)
    def __setattr__(self, name, value):
        if name == 'age' and value < 0:
            print("Нельзя быть младше 0")
            self.__dict__[name] = 0
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        return None
p = Person("Ivan", 30)
print(f"Имя: {p.name}")       
print(f"Возраст: {p.age}") 
p.age = -5                 
print(f"Возраст после попытки установить -5: {p.age}")
print(f"Работа: {p.job}")   
print(f"Адрес: {p.address}")  
print(f"Телефон: {p.phone}")
p.job = "Engineer"
print(f"Работа после установки: {p.job}") 
p.age = 25
print(f"Возраст после установки 25: {p.age}") 