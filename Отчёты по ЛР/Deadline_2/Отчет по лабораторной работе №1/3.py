text = input("Введите свой текст:")
text2 = text.lower().replace(" ", "")
back = 0
forward = len(text2) - 1
palindrom = True
while back < forward and text2[back] == text2[forward]:
    back += 1
    forward -= 1
if back >= forward:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")