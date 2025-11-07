phone_book = {
    "Мария": "1-111-111-11-11",
    "Николай": "2-222-222-22-22", 
    "Иван": "3-333-333-33-33",
    "Марианна": "4-444-444-44-44"}
while True:
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    choice = input("Выберите (1-4):")
    if choice == "1":
        print("\nКонтакты")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    elif choice == "2":
        print("\nНовый контакт")
        name = input("Введите имя:")
        phone = input("Введите номер телефона:")
        phone_book[name] = phone
        print(f"Контакт '{name}' добавлен") 
    elif choice == "3":
        print("\nУдалить")
        name = input("Введите имя контакта для удаления:")
        del phone_book[name]
        print(f"Контакт '{name}' удален")
    elif choice == "4":
        exit()