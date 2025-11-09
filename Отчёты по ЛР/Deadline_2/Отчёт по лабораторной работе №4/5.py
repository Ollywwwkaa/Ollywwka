import string
print("Введите текст (для завершения ввода нажмите Enter дважды):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = " ".join(lines)
words = []
prepinaniya = ""
for char in text:
    if char.isalpha() or char.isdigit():
        prepinaniya += char.lower()
    else:
        if prepinaniya:
            words.append(prepinaniya)
            prepinaniya = ""
if words:
    maxi = words[0]
    mini = words[0]
    for word in words:
        if len(word) > len(maxi):
            maxi = word
        if len(word) < len(mini):
            mini = word
    srednyaya = 0
    for word in words:
        srednyaya += len(word)
    sred = srednyaya / len(words)
    kolichestvo = {}
    for word in words:
            kolichestvo[word] = kolichestvo.get(word, 0) + 1
    sort = sorted(kolichestvo.items(), key=lambda x: x[1], reverse=True)
    slova = sort[:5]
    print(f"\nСамое длинное слово: '{maxi}'")
    print(f"Самое короткое слово: '{mini}'")
    print(f"Средняя длина: {sred:.1f}")
    print(f"Топ-5 слов: {slova}")