text = input("Введите направление(left,right,straight,back):")
if text == "left":
    print("Пойду влево")
elif text == "right":
    print("Пойду вправо")
elif text == "straight":
    print("Пойду прямо")
elif text == "back":
    print("Пойду назад")
else:
    print("Убедитесь в правильности написания направления..")