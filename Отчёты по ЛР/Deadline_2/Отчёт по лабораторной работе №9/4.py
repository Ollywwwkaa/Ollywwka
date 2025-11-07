products = {
    "Ноутбук": {"price": 50000, "sold": 153},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 83}}
max = 0
samyi_prodavaemiy = ""
for product, info in products.items():
    if info["sold"] > max:
        max = info["sold"]
        samyi_prodavaemiy = product
print(f"Самый продаваемый товар: {samyi_prodavaemiy} ({max} шт.)")
viruchka = 0
for product, info in products.items():
    viruchka1 = info["price"] * info["sold"]
    viruchka += viruchka1
print(f"Общая выручка магазина: {viruchka} руб.")
# 3. Наодим товар с наибольшей выручкой
max1 = 0
bolshaya_viruchka = ""
for product, info in products.items():
    viruchka1 = info["price"] * info["sold"]
    if viruchka1 > max1:
        max1 = viruchka1
        bolshaya_viruchka  = product
print(f"Товар с наибольшей выручкой: {bolshaya_viruchka } ({max1} руб.)")