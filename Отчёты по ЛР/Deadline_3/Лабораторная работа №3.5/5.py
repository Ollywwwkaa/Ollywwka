import sys
def create_list(n):
    return [x**2 for x in range(n + 1)]
def create_gen(n):
    return (x**2 for x in range(n + 1))
n = 1000000
lst = create_list(n)
gen = create_gen(n)
print(f"Размер списка: {sys.getsizeof(lst)} байт")
print(f"Размер генератора: {sys.getsizeof(gen)} байт")
# Сложность по памяти:
# Список: O(n) - память растет пропорционально количеству элементов
# Генератор: O(1) - память постоянна, не зависит от количества элементов