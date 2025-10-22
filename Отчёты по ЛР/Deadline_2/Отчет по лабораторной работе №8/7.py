symbol = input("Введите символ для узора прямоугольника:")
visota = int(input("Введите высоту прямоугольника:"))
shirina = int(input("Введите ширину для прямоугольника:"))
stroka = 0
while stroka < visota:
    stroka2 = 0
    while stroka2 < shirina:
        if stroka == 0 or stroka == visota - 1 or stroka2 == 0 or stroka2 == shirina - 1:
            print(symbol, end="")
        else:
            print(" ", end="") 
        stroka2 += 1
    print()
    stroka += 1