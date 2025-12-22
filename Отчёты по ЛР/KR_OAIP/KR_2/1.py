students = {
    "Alice": {"Math": [4, 5, 5], "Physics": [4, 3], "CS": [5, 5, 5]},
    "Bob": {"Math": [3, 4], "Physics": [3, 3], "CS": [4, 3]},
    "Charlie": {"Math": [5, 5], "Physics": [4, 5], "CS": [5, 5]}}
print("Средние баллы учеников:")
for name, subjects in students.items():
    print(f"\n{name}:")
    for subject, grades in subjects.items():
        average = sum(grades) / len(grades)
        print(f"  {subject}: {average:.2f}")
print("Поиск кандидатов на золотую медаль")
medalists = []
for name, subjects in students.items():
    canBeMedalist = True
    for subject, grades in subjects.items():
        for grade in grades:
            if grade < 4:
                canBeMedalist = False
                break
        if subject == "CS":
            csGrades = grades
            csAverage = sum(csGrades) / len(csGrades)
            if csAverage != 5.0:
                canBeMedalist = False
    if canBeMedalist:
        medalists.append(name)
print("Кандидаты на золотую медаль:")
if len(medalists) == 0:
    print("Кандидатов нет")
else:
    for name in medalists:
        allGrades = []
        subjects = students[name]
        for grades in subjects.values():
            allGrades.extend(grades)
        totalAverage = sum(allGrades) / len(allGrades)
        print(f"{name}: общий средний балл = {totalAverage:.2f}")