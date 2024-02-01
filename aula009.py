age = int(input("Qual a sua idade?: "))

if age == 100:
    print("Voce tem um século de vida")
elif age >=18:
    print("Voce é um adulto")
elif age < 0:
    print("Voce ainda não nasceu")
else:
    print("Voce é uma criança")