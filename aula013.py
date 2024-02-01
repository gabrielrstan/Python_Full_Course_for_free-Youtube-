rows = int(input("Qual a quantidade de linhas?: "))
columns = int(input("Qual a quantidade de colunas?: "))
symbol = input("Entre um simbolo para usar ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()