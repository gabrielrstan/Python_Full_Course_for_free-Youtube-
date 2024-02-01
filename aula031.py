import os

path = "pasta/test.txt" 

if os.path.exists(path):
    print("Esse caminho existe")
    if os.path.isfile(path):
        print("Isso é um arquivo")
    elif os.path.isdir(path):
        print("Isso é uma pasta")
else:
    print("Esse caminho não existe")