animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format("cow", "moon"))
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
print("The {animal2} jumped over the {item2}".format(animal2 = "cow", item2 = "moon"))
print("The {0} jumped over the {0}".format(animal, item))

text = "The {} jumped over the {}"

print(text.format(animal, item))

print("\n")

name = "Bro"

print("Hello my name is {}. Nice to meet you".format(name))
print("Hello my name is {:10}. Nice to meet you".format(name))
print("Hello my name is {:>10}. Nice to meet you".format(name))
print("Hello my name is {:<10}. Nice to meet you".format(name))
print("Hello my name is {:^10}. Nice to meet you".format(name))
print("\n")

number = 3.14159
number2 = 1000

print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))
print("The number pi is {:.3f}".format(number))
print("The number  is {}".format(number2))
print("The number  is {:,}".format(number2))
print("The number  is {:b}".format(number2))
print("The number  is {:o}".format(number2))
print("The number  is {:x}".format(number2))
print("The number  is {:X}".format(number2))
print("The number  is {:X}".format(number2))
print("The number  is {:e}".format(number2))
print("The number  is {:E}".format(number2))
