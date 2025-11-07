statistica = {}
print("Введите текст (для завершения введите пустую строку):")
while True:
    line = input()
    if line == "":
        break
    words = line.lower().split()
    for word in words:
        slovo = word.strip('.,!?;:"()')
        if slovo:
            if slovo in statistica:
                statistica[slovo] += 1
            else:
                statistica[slovo] = 1
print(statistica)