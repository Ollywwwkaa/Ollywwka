chislo = int(input("Введите любое число ОБЯЗАТЛЬНО ПОЛОЖИТЕЛЬНОЕ!:"))
peremennayasum = 0
ishodnoechislo = chislo
while chislo > 0:
    cifra = chislo % 10
    peremennayasum += cifra
    chislo = chislo // 10
print(f"Ваше число:{ishodnoechislo}",
      f"Полученный результат из вашего числа: {peremennayasum}")