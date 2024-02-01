class Car:

    color = None

class Motocycle:

    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike1 = Motocycle()

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike1.color)
print()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike1.color)