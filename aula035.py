import os

source = 'test.txt'
destination = 'pasta2/test.txt'

try:
    if os.path.exists(destination):
        print("Ja tem um aquivo no destino")
    else: 
        os.replace(source,destination)
        print(source + " foi movido")
except FileNotFoundError as e:
    print(e)
    print(source + " não encontrado")