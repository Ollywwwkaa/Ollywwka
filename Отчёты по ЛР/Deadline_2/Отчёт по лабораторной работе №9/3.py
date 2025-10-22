text = input("Введите свой произвольный текст:")
bukvi = 0
cifri = 0
znaki = 0
probeli = 0
znaki1 = "!.,?:;-"
for symbols in text:
    if symbols.isalpha():
        bukvi += 1
    elif symbols.isdigit():
        cifri += 1
    elif symbols in znaki1:
        znaki += 1
    elif symbols == " ":
        probeli += 1
print(f"Букв = {bukvi}")
print(f"Цифр = {cifri}")
print(f"Знаков = {znaki}")
print(f"Прбелов = {probeli}")
print(f"Всего букв и символов = {len(text)}")