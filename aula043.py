class Organism:

    alive = True

class Animal(Organism):

    alive = True

    def eat(self):
        print("Este animal esta comendo")

class Dog(Animal):

    def bark(self):
        print("Este cachorro esta latindo")

dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()
