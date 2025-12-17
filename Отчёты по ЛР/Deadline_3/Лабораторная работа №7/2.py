class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = max(salary, 0) 
    @property
    def salary(self):
        """Геттер для зарплаты"""
        return self._salary
    @salary.setter
    def salary(self, value: float):
        """Сеттер для зарплаты с валидацией"""
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной!")
        self._salary = value
    def __repr__(self):
        return f"Employee(name={self.name!r}, salary={self._salary})"
if __name__ == "__main__":
    emp = Employee("John", 50000)
    print(f"Начальная зарплата: {emp.salary}") 
    try:
        emp.salary = -100 
    except ValueError as e:
        print(f"Ошибка: {e}") 
    print(f"Зарплата после попытки установить -100: {emp.salary}")  
    emp.salary = 60000  
    print(f"Зарплата после установки 60000: {emp.salary}") 
    print(emp)