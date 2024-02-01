students = ["João", "Maria", "Antonio", "Daniel", "Matheus"]
students2 = ("João", "Maria", "Antonio", "Daniel", "Matheus")

students.sort()
students2_sorted = sorted(students2)

for i in students:
    print(i)

print()

students.sort(reverse=True)

for i in students:
    print(i)

print()

for i in students2_sorted:
    print(i)

print()

students2_sorted = sorted(students2, reverse=True)

for i in students2_sorted:
    print(i)
