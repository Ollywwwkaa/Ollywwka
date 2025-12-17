virazhenie = input("Введите выражение (Пример: 2 * 5 / 2) ЧЕРЕЗ ПРОБЕЛ!: ")
parts = virazhenie.split()

# Подсчитываем количество операторов
znaki = 0
for part in parts:
    if part in ["+", "*", "-", "/"]:
        znaki += 1

# Обработка выражения с одним оператором
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

# Обработка выражения с двумя операторами
elif znaki == 2:
    ch1 = float(parts[0])
    znak1 = parts[1]
    ch2 = float(parts[2])
    znak2 = parts[3]
    ch3 = float(parts[4])
    
    # Определяем порядок выполнения операций по приоритету
    if (znak2 in ["*", "/"]) and (znak1 in ["+", "-"]):
        # Сначала выполняем вторую операцию (умножение/деление)
        match znak2:
            case "*":
                result = ch2 * ch3
            case "/":
                result = ch2 / ch3
        
        # Затем выполняем первую операцию
        match znak1:
            case "+":
                res = ch1 + result
            case "-":
                res = ch1 - result
            case "*":
                res = ch1 * result
            case "/":
                res = ch1 / result
    else:
        # Выполняем операции слева направо
        match znak1:
            case "+":
                temp_result = ch1 + ch2
            case "-":
                temp_result = ch1 - ch2
            case "*":
                temp_result = ch1 * ch2
            case "/":
                temp_result = ch1 / ch2
        
        match znak2:
            case "+":
                res = temp_result + ch3
            case "-":
                res = temp_result - ch3
            case "*":
                res = temp_result * ch3
            case "/":
                res = temp_result / ch3
    
    print(f"Ваш полученный результат = {res}")

else:
    print("Некорректное выражение! Используйте 1 или 2 оператора.")