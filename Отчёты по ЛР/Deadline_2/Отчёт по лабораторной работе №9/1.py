fruits = {
    "яблоки": 5,
    "бананы": 3,
    "апельсины": 10,
    "арбузы": 33}
print("Начало")
for fruit, quantity in fruits.items():
    print(f"За прилавком есть {quantity} {fruit}")
fruits["яблоки"] = fruits["яблоки"] - 2
fruits["арбузы"] = 0
print("После обновления")
for fruit, quantity in fruits.items():
    print(f"За прилавком осталось {quantity} {fruit}")