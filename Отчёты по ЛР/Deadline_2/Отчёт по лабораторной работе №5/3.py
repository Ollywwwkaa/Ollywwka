colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128)}
red = colors["красный"]
blue = colors["синий"]
mix_r = (red[0] + blue[0]) // 2
mix_g = (red[1] + blue[1]) // 2
mix_b = (red[2] + blue[2]) // 2
mixed_color = (mix_r, mix_g, mix_b)
print(f"красный {red} и синий {blue}")
print(f"фиолетовый: {mixed_color}")
green = colors["зеленый"]
invert = (255 - green[0], 255 - green[1], 255 - green[2])
print(f"\nИнвертируем зеленый {green}")
print(f"Получаем: {invert}")