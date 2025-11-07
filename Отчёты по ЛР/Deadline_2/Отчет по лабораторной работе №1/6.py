symbol = input("Введите символ для узора прямоугольника:")
visota = int(input("Введите высоту прямоугольника:"))
shirina = int(input("Введите ширину для прямоугольника:"))
stroka = 0
while stroka < visota:
    stroka1 = 0
    while stroka1 < shirina:
        print(symbol, end="")
        stroka1 += 1
    print()
    stroka += 1