class Animal:

    def eat(self):
        print("Este animal esta comendo")

    

class Rabbit(Animal):
    
    def eat(self):
        print("Este coelho esta comendo uma cenoura")


rabbit = Rabbit()
rabbit.eat()