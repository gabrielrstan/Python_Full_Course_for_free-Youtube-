try:
    numerator = int(input("Entre com um numero que será o dividento: "))
    denominator = int(input("Entre com um numero que será o divisor: "))
    result = numerator/denominator

except ZeroDivisionError as e:
    print(e)
    print("Voce não pode dividir por zero")
except ValueError as e:
    print(e)
    print("Utilize apenas numeros")
#except Exception as e:
#    print(e)
 #   print("Algo deu errado")
else:
    print(result)

finally:
    print("Isto sempre será executado")
