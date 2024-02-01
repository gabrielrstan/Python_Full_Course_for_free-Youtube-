class Car:

    def turn_on(self):
        print("Voce iniciou o motor")
        return self

    def turn_off(self):
        print("Voce desligou o motor")
        return self

    def drive(self):
        print("Voce dirige o carro")
        return self

    def brake(self):
        print("Voce pisou no freio")
        return self

car = Car()
car.turn_off()
car.drive()
car.brake()\
    .turn_off()
print()
car.turn_on()\
    .drive()\
        .brake()\
            .turn_off()