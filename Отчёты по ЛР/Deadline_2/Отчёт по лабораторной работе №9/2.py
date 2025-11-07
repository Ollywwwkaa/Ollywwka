text = input("Введите произвольный текст: ")
text1 = text.lower()
slovar1 = {}
for slovar in text1:
    if slovar in slovar1:
        slovar1[slovar] += 1
    else:
        slovar1[slovar] = 1
print(slovar1)