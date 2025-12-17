import time
print("Создание списка из 100 000 элементов...")
original_list = list(range(100_000))
print("\nТестирование pop(0) - удаление из начала списка")
list1 = original_list.copy()  
start_time = time.time()
for i in range(1000):
    list1.pop(0)
pop0_time = time.time() - start_time
print(f"Время выполнения 1000 операций pop(0): {pop0_time:.6f} секунд")
print("\nТестирование pop() - удаление с конца списка")
list2 = original_list.copy() 
start_time = time.time()

for i in range(1000):
    list2.pop()
pop_time = time.time() - start_time
print(f"Время выполнения 1000 операций pop(): {pop_time:.6f} секунд")
print("\n" + "="*50)
print("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:")
print("="*50)
print(f"pop(0) - удаление из начала: {pop0_time:.6f} сек")
print(f"pop()  - удаление с конца:   {pop_time:.6f} сек")
if pop_time > 0:
    ratio = pop0_time / pop_time
    print(f"\npop(0) медленнее pop() в {ratio:.2f} раз")
print("\n" + "="*50)
print("ВЫВОД О СЛОЖНОСТИ ОПЕРАЦИЙ:")
print("="*50)
print("1. pop() - удаление с конца списка:")
print("   Сложность: O(1)")
print("   Причина: удаление последнего элемента не требует перемещения")
print("           остальных элементов")
print("\n2. pop(0) - удаление из начала списка:")
print("   Сложность: O(n)")
print("   Причина: удаление первого элемента требует перемещения ВСЕХ")
print("           оставшихся n-1 элементов на одну позицию назад")
print("\nОбщий вывод:")
print("- pop() работает за константное время O(1)")
print("- pop(0) работает за линейное время O(n)")
print("- При n=100000 pop(0) значительно медленнее pop()")