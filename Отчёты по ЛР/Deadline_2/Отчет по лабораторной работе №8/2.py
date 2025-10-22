end = 0
while True:
    chislo = int(input("Введите свое число:"))
    if chislo > 0:
        end +=1
    else:
        break
print(f"Чисел до нуля:{end}")