text =  input("Введите свой произвольный текст:")
oldtxt, newtxt = input("Что заменить на что?:").split()
print(text.replace(oldtxt, newtxt))