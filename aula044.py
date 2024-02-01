class Prey:

    def flee(self):
        print("Este animal foge")   

class Pretador:

    def hunt(self):
        print("Esse animal esta caçando")

class Rabbit(Prey):
    
    pass

class Fish(Prey, Pretador):

    pass

class Hawk(Pretador):
    
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()