class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError("Можно складывать только векторы")
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError("Можно вычитать только векторы")
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other) -> 'Vector | float':
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Умножение поддерживается только на число или вектор")
    def __rmul__(self, other) -> 'Vector | float':
        return self.__mul__(other)
    def __eq__(self, other: 'Vector') -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
if __name__ == "__main__":
    v1 = Vector(2, 3)
    v2 = Vector(4, 1)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 3)  
    print(3 * v1)  
    print(v1 * v2)  
    print(v1 == Vector(2, 3)) 
    print(v1 == v2)