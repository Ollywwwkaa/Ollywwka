class StringUtils:
    @staticmethod
    def invert(string: str) -> str:
        return string[::-1]
    @staticmethod
    def normalize(string: str) -> str:
        return string.strip().lower()
class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
    @classmethod
    def from_string(cls, data_string: str):
        try:
            name, role = data_string.split(';', maxsplit=1)
            return cls(name.strip(), role.strip())
        except ValueError:
            raise ValueError(f"Некорректный формат строки: {data_string}. "
                           f"Ожидается формат: 'Имя;Роль'")
    def __repr__(self) -> str:
        return f"User(name='{self.name}', role='{self.role}')"
if __name__ == "__main__":
    print(StringUtils.invert("Hello")) 
    print(StringUtils.invert("Python"))  
    print(StringUtils.normalize("  DATA  "))  
    print(StringUtils.normalize("  HELLO WORLD  "))  
    print(StringUtils.normalize("PyThOn"))  
    user = User.from_string("Alice;Admin")
    print(user.name)  
    print(user.role)  
    user2 = User.from_string("Bob;User")
    print(user2) 
    user3 = User("Charlie", "Moderator")
    print(user3) 
    try:
        bad_user = User.from_string("OnlyName")
    except ValueError as e:
        print(f"Ошибка: {e}")