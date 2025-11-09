students = [
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Мария", 19, 4.8),
    ("Иван", 20, 4.1),
    ("Елена", 23, 4.6)]
for student in students:
    print(f"- {student[0]} ({student[1]} лет), средний балл: {student[2]}")
print("\nстарше 20 лет:")
for name, age, srball in students:
    if age > 20:
        print(f"- {name} ({age}), средний балл: {srball}")
stud = students[0]
for student in students:
    if student[2] > stud[2]:
        stud = student
print(f"\nЛучший: {stud[0]}, средний балл: {stud[2]}")
sort = sorted(students, key=lambda x: x[0])
print("\nСтуденты отсортированные по имени:")
for name, age, srball in sort:
    print(f"- {name} ({age} лет), средний балл: {srball}")