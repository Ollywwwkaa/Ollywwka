virazhenie = input("Введите выражение (Пример: 2*5/2) ЧЕРЕЗ ПРОБЕЛ!:")
parts = virazhenie.split()
znaki = 0
for part in parts:
    if part in ["+", "*", "-", "/"]:
        znaki += 1
if znaki == 1:
    ch1 = float(parts[0])
    znak = parts[1]
    ch2 = float(parts[2])
    match znak:
        case "+":
            res = ch1 + ch2
        case "-":
            res = ch1 - ch2
        case "*":
            res = ch1 * ch2
        case "/":
            res = ch1 / ch2
    print(f"Ваш полученный результат = {res}")
elif znaki == 2:
    ch1 = float(parts[0])
    znak1 = parts[1]
    ch2 = float(parts[2])
    znak2 = parts[3]
    ch3 = float(parts[4])
if znak1 in ["*", "/"]:
    match znak1:
        case "*":
            result = ch1 * ch2
        case "/":
            result = ch1 / ch2
    match znak2:
        case "+":
            res = result + ch3
        case "-":
            res = result - ch3
        case "/":
            res = result / ch3
        case "*":
            res = result * ch3
else:
    match znak2:
        case "/":
            result2 = ch2 / ch3
        case "*":
            result2 = ch2 * ch3
        case "+":
            result2 = ch2 + ch3
        case "-":
            result2 = ch2 - ch3
    match znak1:
        case "-":
            res = ch1 - result2
        case "+":
            res = ch1 + result2
print(f"Ваш полученный результат = {res}")