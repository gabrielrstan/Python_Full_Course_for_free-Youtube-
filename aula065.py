import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logado em: {} segundos".format(count))

x = threading.Thread(target=timer, daemon=True)
x.start()

#x.setDaemon(True)
print(x.isDaemon())

answer = input("Voce deseja sair? ")