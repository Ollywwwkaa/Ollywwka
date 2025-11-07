text = input("Введите свой текст:")
glasnie = "АЕЁИОУЫЭЮЯаеёиоуыэюяaeAEIOUiou"
res = ""
i = 0
while i < len(text):
    if text[i] not in glasnie:
        res += text[i]
    i += 1
print("Результат:", res)
