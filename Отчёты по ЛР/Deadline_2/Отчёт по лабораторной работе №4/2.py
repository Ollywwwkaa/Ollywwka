chisla = [10, 20, 30, 40, 12, 45, 69, 11, 15]
chetnie = []
for num in chisla:
    if num % 2 == 0:
        chetnie.append(num)
print("Четные числа:", chetnie)
bolshie = [num for num
           in chisla if num > 50]
print("Числа больше 50:", bolshie)