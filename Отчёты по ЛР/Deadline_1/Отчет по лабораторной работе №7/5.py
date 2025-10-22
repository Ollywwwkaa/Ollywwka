import math
text = input("Введите число1 ЗНАК число2:(Через пробел!):")
razdelenie = text.split()
symbols1 = float(razdelenie[0])
znak = razdelenie[1]
symbols2 = float(razdelenie[2])
if znak == "*":
   itog = symbols1 * symbols2
   print(f"Результат: {symbols1} * {symbols2} = {itog}")
elif znak == "/":
    itog = symbols1 / symbols2
    print(f"Результат: {symbols1} / {symbols2} = {itog}")
elif znak == "+":
    itog = symbols1 + symbols2
    print(f"Результат: {symbols1} + {symbols2} = {itog}")
elif znak == "-":
    itog = symbols1 - symbols2
    print(f"Результат: {symbols1} - {symbols2} = {itog}")
elif znak == "%":
    itog = symbols1 % symbols2
    print(f"Результат: {symbols1} % {symbols2} = {itog}")
elif znak == "//":
    itog = symbols1 // symbols2
    print(f"Результат: {symbols1} // {symbols2} = {itog}")
elif znak == "**":
    itog = symbols1 ** symbols2
    print(f"Результат: {symbols1} ** {symbols2} = {itog}")
elif znak == "%%":
    itog = (symbols2 / 100) * symbols1
    print(f"Результат: {symbols2}% от {symbols1} = {itog}")
elif znak == "/**":
    itog = math.sqrt(symbols1)
    print(f"Результат: корень из {symbols1} = {itog}")
else:
    print("Ошибка! Неизвестная операция. Проверьте, корректны ли числа?..")