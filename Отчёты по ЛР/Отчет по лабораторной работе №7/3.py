text = input("Введите произвольный текст:")
slovo = input("Введите слово:")
if slovo in text:
    poisk = text.count(slovo)
    print(f"Слово <{slovo}> найдено в тексте. Ваше слово:")
    print(f"Количество повторений:<{poisk}>" )
else:
    print(f"Введенное вами слово не найдено в тексте. Повторите попытку")