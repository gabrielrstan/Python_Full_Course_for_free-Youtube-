temp = int(input("Qual a temperatura agora?: "))

if not(temp >= 0 and temp <= 30):
    print("A temperatura esta ruim hoje")
    print("Fique em casa")
elif not(temp < 0 or temp > 30):
    print("A temperatura esta boa hoje")
    print("Vá passear ")