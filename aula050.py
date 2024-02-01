class Duck:

    def walk(self):
        print("O pato esta andando")

    def talk(self):
        print("O pato esta grasnando")

class Chicken:

     def walk(self):
        print("A galinha esta andando")

     def talk(self):
        print("A galinha esta cacarejando")

class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("Voce pegou o animal")
    
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
print()
person.catch(chicken)