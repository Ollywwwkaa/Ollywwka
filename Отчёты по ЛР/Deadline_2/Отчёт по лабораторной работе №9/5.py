kolichestvo = int(input("Введите количество чисел:"))
chisla = []
for i in range(kolichestvo):
    chislo = float(input(f"Введите число {i+1}: "))
    chisla.append(chislo)
if kolichestvo > 0:
    max = max(chisla)
    min = min(chisla)   
    srednee = sum(chisla) / kolichestvo  
    kolichestvo1 = 0
for chislo in chisla:
     if chislo > srednee:
        kolichestvo1 += 1
print(f"\nМаксимальное: {max}")
print(f"Минимальное: {min}")
print(f"Среднее: {srednee:.2f}")
print(f"Чисел больше среднего: {kolichestvo1}")