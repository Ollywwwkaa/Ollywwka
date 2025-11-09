import string
print("Введите текст в конце пустая строка:")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = " ".join(lines)
words = []
slovo = ""
for char in text:
    if char.isalpha() or char.isdigit():
        slovo += char.lower()
    else:
        if slovo:
            words.append(slovo)
            slovo = ""
if slovo:
    words.append(slovo)
if words:
    long = words[0]
    short = words[0]
    for word in words:
        if len(word) > len(long):
            long = word
        if len(word) < len(short):
            short = word
    srednee = 0
    for word in words:
        srednee += len(word)
    sred = srednee / len(words)
    kolichestvo = {}
    for word in words:
        kolichestvo[word] = kolichestvo.get(word, 0) + 1
    sort = sorted(kolichestvo.items(), key=lambda x: x[1], reverse=True)
    slova = sort[:5]
    print(f"\nСамое длинное: '{long}'")
    print(f"Самое короткое: '{short}'")
    print(f"Средняя: {sred:.1f}")
    print(f"5 слов: {slova}")