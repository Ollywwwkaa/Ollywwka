import random
chislobot = random.randint(1,100)
print("BOT:: Угадай мое число :P")
while True:
    igrok = int(input("Введи число и попробуй угарадть :) :"))
    if igrok < chislobot:
        print("Больше :р")
    elif igrok > chislobot:
        print("Меньше :0")
    else:
        print(f"Ты угадал моё число {chislobot}...")
        break