text = input("Придумайте и введите пароль:")
text2 = input("Повторите придуманный вами пароль")
if text == text2:
    print("Успешно")
else:
    print("Повторите попытку снова..")
text3 = input("Для авторизации введите пароль")
if text == text3:
    print("Access")
else:
    print("Denied")