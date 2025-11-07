ToDoList = []
while True:
    print("1 - Показать")
    print("2 - Добавить")
    print("3 - Удалить")
    print("4 - Выйти")
    deystvie = input("Выберите(1-4): ")
    if deystvie == "1":
        print("\nЗадачи")
        if len(ToDoList) == 0:
            print("Список задач пуст")
        else:
            for i, task in enumerate(ToDoList, 1):
                print(f"{i}. {task}")
    elif deystvie == "2":
        print("\nДобавить")
        new_task = input("Введите описание задачи:")
        ToDoList.append(new_task)
        print(f"Задача '{new_task}' добавлена")
    elif deystvie == "3":
        print("\nУдалить")
        if len(ToDoList) == 0:
            print("Список задач пуст")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(ToDoList, 1):
                print(f"{i}. {task}")
                task_number = int(input("\n Введите номер: "))
                if 1 <= task_number <= len(ToDoList):
                    removed_task = ToDoList.pop(task_number - 1)
                    print(f'Задача "{removed_task}" удалена')
                else:
                    print("Неправильный номер задачи")
    elif deystvie == "4":
        break