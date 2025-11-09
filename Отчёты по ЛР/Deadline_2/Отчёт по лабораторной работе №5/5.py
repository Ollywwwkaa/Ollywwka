math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}
print("по курсам:")
print(f"Математика: {math_students}")
print(f"Физика: {physics_students}")
print(f"Компьютерные науки: {cs_students}")
all = math_students & physics_students & cs_students
print(f"\nпосещают все три курса: {all}")
only = math_students - physics_students - cs_students
physics = physics_students - math_students - cs_students
cs = cs_students - math_students - physics_students
onlyone = only | physics | cs
print(f"посещают только один курс: {onlyone}")
notphysics = math_students - physics_students
print(f"посещают математику, но не физику: {notphysics}")
students = math_students | physics_students | cs_students
kolvo = len(students)
print(f"уникальных студентов: {kolvo}")
print(f"Все: {students}")