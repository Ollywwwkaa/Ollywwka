def task_1(arr):
    for i in arr:
        if i == 100:
            return True
    return False
# Сложность: O(n) - линейный поиск в худшем случае проходит по всем n элементам массива
def task_2(arr):
    return arr[0] + arr[-1]
# Сложность: O(1) - доступ к элементам по индексу занимает константное время
def task_3(arr):
    count = 0
    for i in arr:
        for j in arr:
            if i == j:
                count += 1
    return count
# Сложность: O(n²) - вложенные циклы дают n * n = n² операций в худшем случае