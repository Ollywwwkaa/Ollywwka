import time
import random
def find_duplicates_quadratic(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                if arr[i] not in duplicates:
                    duplicates.append(arr[i])
    return duplicates
def measure_execution_time(size):
    print(f"Размер списка: {size}")
    arr = [random.randint(0, size // 10) for _ in range(size)]
    print(f"Сгенерирован список из {size} элементов")
    print(f"Диапазон значений: от 0 до {size // 10}")
    start_time = time.time()
    duplicates = find_duplicates_quadratic(arr)
    execution_time = time.time() - start_time
    print(f"Найдено дубликатов: {len(duplicates)}")
    print(f"Время выполнения: {execution_time:.4f} секунд")
    return execution_time, len(duplicates)
def main():
    print("ДЕМОНСТРАЦИЯ ПРОБЛЕМЫ ВЛОЖЕННЫХ ЦИКЛОВ O(n²)")
    print("Функция find_duplicates_quadratic() имеет сложность O(n²)")
    print("При увеличении n в k раз, время должно увеличиться в ~k² раз\n")
    size1 = 5000
    size2 = 10000
    time1, dup1 = measure_execution_time(size1)
    time2, dup2 = measure_execution_time(size2)
    if time1 > 0:
        time_ratio = time2 / time1
        size_ratio = size2 / size1
        expected_ratio = size_ratio ** 2 
        print("АНАЛИЗ РЕЗУЛЬТАТОВ:")
        print(f"Размер данных увеличен в {size_ratio:.1f} раза (с {size1} до {size2})")
        print(f"Ожидаемый рост времени для O(n²): {expected_ratio:.1f} раза")
        print(f"Фактический рост времени: {time_ratio:.1f} раза")
        print(f"\nОжидаемое время для {size2} элементов:")
        print(f"  {expected_ratio:.1f} × {time1:.4f} сек = {expected_ratio * time1:.4f} сек")
        print(f"Фактическое время для {size2} элементов: {time2:.4f} сек")
        print("ПОЧЕМУ ТАК ПРОИСХОДИТ:")
        print("Сложность O(n²) означает, что при увеличении n:")
        print(f"- Для n = {size1}: выполняется ~{size1} × {size1} = {size1**2:,} операций")
        print(f"- Для n = {size2}: выполняется ~{size2} × {size2} = {size2**2:,} операций")
        print(f"Количество операций увеличилось в {(size2**2)/(size1**2):.1f} раза")
        print("ОТВЕТ НА ВОПРОС ЗАДАНИЯ:")
        print(f"При увеличении данных в 2 раза (с {size1} до {size2} элементов),")
        print(f"время выполнения увеличилось примерно в {time_ratio:.1f} раза.")
        print(f"Для O(n²) алгоритма ожидается увеличение в {expected_ratio:.1f} раза.")
        print(f"\nВывод: Вложенные циклы становятся непрактичными на больших данных,")
        print(f"так как при росте данных время растет в квадратичной зависимости.")
        print("АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ:")
        print("Для поиска дубликатов лучше использовать:")
        print("1. set() - сложность O(n) для создания и O(1) для проверки наличия")
        print("2. dict() или Counter из collections - сложность O(n)")
        print("3. Сортировка + один проход - сложность O(n log n)")
    else:
        print("Ошибка: время выполнения слишком мало для точного измерения")
if __name__ == "__main__":
    main()