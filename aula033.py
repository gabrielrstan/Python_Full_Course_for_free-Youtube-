'''text = "Yooooo\nThis is some text\nHave as good one!\n"

try:
    with open('pasta/test.txt', 'w') as file:
        print(file.write(text))

except FileNotFoundError as e:
    print(e)'''

text = "Have a nice day! See ya"

try:
    with open('pasta/test.txt', 'a') as file:
        print(file.write(text))

except FileNotFoundError as e:
    print(e)