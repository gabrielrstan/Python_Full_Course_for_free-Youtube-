import random
while True:
    choices = ["pedra", "papel", "tesoura"]

    computer = random.choice(choices)
    player = None
    #print(computer)

    while player not in choices:
        player = input("Pedra, Papel ou Tesoura?: ").lower()

    if player == computer:
        print("Computador: ", computer)
        print("Jogador: ", player)
        print("Empate")
    elif player == "pedra":
        if computer == "tesoura":
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Voce Venceu")
        elif computer == "papel":
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Voce Perdeu")
    elif player == "papel":
        if computer == "pedra":
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Voce Venceu")
        elif computer == "tesoura":
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Voce Perdeu")
    elif player == "tesoura":
        if computer == "papel":
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Voce Venceu")
        elif computer == "pedra":
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Voce Perdeu")
    player_again = input("Jogar novamente? (sim/não) ").lower()

    if player_again != "sim":
        break

print("Tchau!")