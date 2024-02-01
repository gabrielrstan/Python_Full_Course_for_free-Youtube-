class Animal:

    alive = True

    def eat(self):
        print("Este animal esta comendo")

    def slumber(self):
        print("Este animal esta dormindo")


class Rabbit(Animal):
    
    def run(self):
        print("Este coelho esta correndo")

class Fish(Animal):

    def swim(self):
        print("Este peixe esta nadando")

class Hawk(Animal):
    
    def fly(self):
        print("Este falcão esta voando")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.slumber()
rabbit.run()
fish.swim()
hawk.fly()