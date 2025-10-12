message = input("Введите свое сообщение:")
symbols = int(input("Введите ваше количество подстановочных символов:"))
import random
import string
def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
random_chars = generate_random_string(10)
print(random_chars)