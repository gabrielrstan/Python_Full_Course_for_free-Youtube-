'''def double(x):
    return x * 2'''

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda firt_name, last_name: firt_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(2, 3))
print(add(3, 8, 9))
print(full_name("Gabriel", "Stanzione"))
print(age_check(25))