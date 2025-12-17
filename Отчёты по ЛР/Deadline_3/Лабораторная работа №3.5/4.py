import time
import random
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None
def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
def generate_test_data(size, min_val=0, max_val=10000):
    random.seed(42)
    arr = [random.randint(min_val, max_val) for _ in range(size)]
    idx1, idx2 = random.sample(range(size), 2)
    target = arr[idx1] + arr[idx2]
    random.shuffle(arr)
    return arr, target, (arr[idx1], arr[idx2])
def measure_performance():
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ПОИСКА ПАРЫ ЧИСЕЛ")
    size = 10000
    print(f"Размер тестового массива: {size:,} элементов")
    print("\nГенерация тестовых данных...")
    arr, target, expected_pair = generate_test_data(size, 0, 100000)
    print(f"Целевая сумма (target): {target}")
    print(f"Ожидаемая пара: {expected_pair}")
    print("ТЕСТИРОВАНИЕ МЕДЛЕННОЙ ФУНКЦИИ (O(n²)):")
    start_time = time.time()
    result_slow = find_pair_slow(arr, target)
    time_slow = time.time() - start_time
    print(f"Найдена пара: {result_slow}")
    print(f"Время выполнения: {time_slow:.6f} секунд")
    print("ТЕСТИРОВАНИЕ БЫСТРОЙ ФУНКЦИИ (O(n)):")
    start_time = time.time()
    result_fast = find_pair_fast(arr, target)
    time_fast = time.time() - start_time
    print(f"Найдена пара: {result_fast}")
    print(f"Время выполнения: {time_fast:.6f} секунд")
    print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ:")
    if result_slow and result_fast:
        sorted_slow = tuple(sorted(result_slow))
        sorted_fast = tuple(sorted(result_fast))
        sorted_expected = tuple(sorted(expected_pair))
        print(f"Обе функции нашли корректную пару: {'ДА' if sorted_slow == sorted_expected else 'НЕТ'}")
        print(f"Найденные пары одинаковы: {'ДА' if sorted_slow == sorted_fast else 'НЕТ'}")
        print(f"Сумма найденной пары равна target: {sum(result_slow) == target}")
    if time_fast > 0:
        speedup = time_slow / time_fast
        print(f"\nБыстрая функция быстрее медленной в {speedup:.2f} раз!")
    else:
        print(f"\nБыстрая функция выполнилась менее чем за 0.000001 секунд")
    print("АНАЛИЗ СЛОЖНОСТИ АЛГОРИТМОВ:")
    print("МЕДЛЕННЫЙ АЛГОРИТМ (find_pair_slow):")
    print("  Сложность: O(n²)")
    print("  Причина: два вложенных цикла, каждый по n элементов")
    print(f"  Примерное количество операций для n={size}: ~{size}×{size} = {size**2:,}")
    print(f"\nБЫСТРЫЙ АЛГОРИТМ (find_pair_fast):")
    print("  Сложность: O(n)")
    print("  Причина: один проход по массиву, поиск в set - O(1)")
    print(f"  Примерное количество операций для n={size}: ~{size}")
    print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ:")
    sizes = [1000, 2000, 5000, 10000]
    print(f"\nЗависимость времени от размера данных:")
    print(f"{'Размер':<10} {'O(n²) время':<15} {'O(n) время':<15} {'Ускорение':<10}")
    for s in sizes:
        test_arr, test_target, _ = generate_test_data(s, 0, 10000)
        start = time.time()
        find_pair_slow(test_arr, test_target)
        t_slow = time.time() - start
        start = time.time()
        find_pair_fast(test_arr, test_target)
        t_fast = time.time() - start
        speedup = t_slow / t_fast if t_fast > 0 else float('inf')
        print(f"{s:<10} {t_slow:<15.6f} {t_fast:<15.6f} {speedup:<10.1f}")
def demonstrate_algorithm():
    print("ДЕМОНСТРАЦИЯ РАБОТЫ БЫСТРОГО АЛГОРИТМА:")
    example_arr = [3, 5, 7, 2, 8, 1]
    example_target = 10
    print(f"Массив: {example_arr}")
    print(f"Целевая сумма: {example_target}")
    print("\nПошаговое выполнение:")
    seen = set()
    for i, num in enumerate(example_arr):
        complement = example_target - num
        print(f"\nШаг {i+1}: число = {num}")
        print(f"  complement = {example_target} - {num} = {complement}")
        print(f"  seen = {seen}")
        if complement in seen:
            print(f"  ✓ Найдена пара! {complement} + {num} = {example_target}")
            print(f"  Результат: ({complement}, {num})")
            break
        else:
            seen.add(num)
            print(f"  Добавляем {num} в seen")
def main():
    demonstrate_algorithm()
    measure_performance()
    print("ИТОГОВЫЙ ВЫВОД:")
    print("1. Быстрая функция (find_pair_fast) использует set для хранения")
    print("   уже просмотренных чисел, что позволяет:")
    print("   - Иметь сложность O(n) вместо O(n²)")
    print("   - Работать в десятки/сотни раз быстрее на больших данных")
    print("\n2. Ключевая идея: для каждого числа проверяем, есть ли в set")
    print("   complement = target - num")
    print("\n3. Этот подход работает, потому что:")
    print("   - Поиск в set имеет сложность O(1) в среднем случае")
    print("   - Мы проходим по массиву всего один раз")
    print("\n4. На списке из 10,000 элементов ускорение составляет")
    print("   сотни или тысячи раз (в зависимости от аппаратного обеспечения)")
if __name__ == "__main__":
    main()