students = [("João", "B", 60),
            ("Maria", "A", 38),
            ("Antonio", "A", 45),
            ("Daniel", "B", 22),
            ("Matheus", "E", 88)]

students.sort()

for i in students:
    print(i)

grade = lambda grades:grades[1]
students.sort(key=grade)
print()

for i in students:
    print(i)

students.sort(key=grade, reverse=True)
print()

for i in students:
    print(i)
    
print()

age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)

students.sort(key=age, reverse=True)
print()


for i in students:
    print(i)

students2 = (("João", "B", 60),
            ("Maria", "A", 38),
            ("Antonio", "A", 45),
            ("Daniel", "B", 22),
            ("Matheus", "E", 88))
print()

sorted_students = sorted(students2, key=age)

for i in sorted_students:
    print(i)