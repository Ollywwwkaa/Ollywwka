from math import sqrt
a = (3, 7)
b = (10, 2)
x1, y1 = a
x2, y2 = b
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"A: {a}")
print(f"B: {b}")
print(f"Расстояние: {distance:.2f}")