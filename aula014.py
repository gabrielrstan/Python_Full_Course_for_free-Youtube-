while True:
    name = input("Entre o seu nome: ")
    if name != "":
        break

phone_number = "123-456-7890"

for j in phone_number:
    if j == "-":
        continue
    print(j, end="")

for k in range(1,21):
    if k == 13:
        pass
    else:
        print(k)