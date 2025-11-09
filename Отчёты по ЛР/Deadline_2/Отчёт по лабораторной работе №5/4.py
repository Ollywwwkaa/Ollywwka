import string
text = input("Введите свой текст: ")
znaki = str.maketrans('', '', string.punctuation)
clear = text.translate(znaki).lower()
words = clear.split()
unicalnie = set(words)
print(f"\nУникальные: {len(unicalnie)}")
print(f"Все: {unicalnie}")
long = {word for word in unicalnie if len(word) > 5}
print(f"Длинные: {long}")
key = {"python", "programming"}
found = key & unicalnie
print(f"\nключевые слова: {bool(found)}")
if found:
    print(f"Конкретно найдены: {found}")