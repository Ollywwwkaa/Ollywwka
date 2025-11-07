statistica = {}
print("Введите текст (для завершения введите пустую строку):")
while True:
    line = input()
    words = line.lower().split()
    for word in words:
        word = word.strip('.,!?;:"()')
        if word:
            if word in statistica:
                statistica[word] += 1
        else:
            statistica[word] = 1
print(statistica)