# ---------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Entre (A, B, C ou D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
# ---------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRETO")
        return 1
    else:
        print("ERRADO")
        return 0
# ---------------------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------------------")
    print("RESULTADO")
    print("---------------------------------------")
    print("Respostas: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
   
    print("Palpites: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("O placar final é: {}%".format(score))
# ---------------------------------------
def play_again():
    response = input("|Voce quer jogar novamente? (sim ou não)")
    response = response.upper()
    if response == "SIM":
        return True
    else:
        return False
# ---------------------------------------

questions = {
    "Quem criou o Python?: " : "A",
    "Qual ano o Python foi criado?: " : "B",
    "Python é homenageado a qual grupo de comédia?: " : "C",
    "A Terra é redonda? ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. Sim", "B. Não", "C. As Vezes", "D. O que é terra?"]
    ]

new_game()

while play_again():
    new_game()

print("Tchau")