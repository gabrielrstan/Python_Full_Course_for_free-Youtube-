try:
    with open('pasta/test.txt') as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)

#print(file.closed)
