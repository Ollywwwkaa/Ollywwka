god = int(input("Введите год:"))
if god % 4 != 0:
    print(f"год :{god} невисокосный.")
elif god % 100 != 0:
    print(f"год :{god} високосный.")
elif god % 400 != 0:
    print(f"год :{god} невисокосный.")
else:
     print(f"год :{god} високосный.")