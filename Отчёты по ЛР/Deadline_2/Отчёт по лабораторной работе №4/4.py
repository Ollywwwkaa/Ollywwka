temperatura = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
max = max(temperatura)
min = min(temperatura)
temps = sum(temperatura) / len(temperatura)
days = len([temp for temp in temperatura if temp > temps])
sorted = sorted(temperatura)
print("\nРезультат:")
print(f"• Максимальная: {max}")
print(f"• Минимальная: {min}")
print(f"• Средняя: {temps:.1f}")
print(f"• Количество дней с температурой выше средней: {days}")
print(f"• Отсортированный : {sorted}")
temperatures = [temp * 9/5 + 32 for temp in temperatura]
print(f"\n B Фаренгейтах: {[round(temp, 1) for temp in temperatures]}")