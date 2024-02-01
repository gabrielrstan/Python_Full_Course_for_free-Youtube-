student = ("Gabriel", 27, "male")

print(student.count("Gabriel"))
print(student.index("male"))

for x in student:
    print(x)

if "Gabriel" in student:
    print("Gabriel esta aqui")