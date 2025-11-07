fructs = {
    "яблоки": 5,
    "бананы": 3,
    "апельсины": 10,
    "арбузы": 33}
print("Начало")
for fructs, quantity in fructs.items():
    print(f"За прилавком есть {quantity} {fructs}")
fructs["яблоки"] = fructs["яблоки"] - 2
fructs["арбузы"] = 0
print("Обновленный словарь")
for fructs, quantity in fructs.items():
    print(f"За прилавком осталось {quantity} {fructs}")