def hello(**names): #convenção usar **kwargs
    print("Hello " + names['first'] + " " + names['last'])
    print("\n")
    print("Hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")

hello(title = "Mr", first="Bro",middle="Dude", last="Code")

