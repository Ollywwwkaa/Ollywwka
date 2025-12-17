class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def strike(self, target):
        target.health -= self.attack_power
knight = Hero("Arthur", 100, 20)
rogue = Hero("Robin", 80, 15)
knight.strike(rogue)  # Артур бьет Робина
rogue.strike(knight)  # Робин бьет Артура
print(f"{knight.name}: {knight.health}")
print(f"{rogue.name}: {rogue.health}")