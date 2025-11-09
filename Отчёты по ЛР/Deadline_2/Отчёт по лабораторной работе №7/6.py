from typing import List, Any

def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:# Находит общие элементы между двумя списками без дубликатов.
    # Преобразуем списки в множества для удаления дубликатов и находим пересечение
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1 & set2  # или set1.intersection(set2)
    # Преобразуем обратно
    return list(common_elements)
# Тестируем функцию
list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]
common = find_common_elements(list1, list2)
print(common)  # Вывод: [4, 5] (порядок может отличаться)