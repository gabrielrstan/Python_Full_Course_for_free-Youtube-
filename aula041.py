from aula040b import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)

Car.wheels = 3

print(car_1.wheels)
print(car_2.wheels)
