squares = []

for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares2 = [i * i for i in range(1, 11)]
print(squares2)
print()
print()

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x > 60, students))
print(passed_students)

passed_students2 = [i for i in students if i >= 60]
print(passed_students2)

passed_students3 = [i if i>=60 else "FAILED" for i in students ]
print(passed_students3)