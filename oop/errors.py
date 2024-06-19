
try : 
    numero1 = 3
    numero2 = 0

    resultado = numero1 / numero2
    print(resultado)

except Exception as exception:
    print(exception)
    print(isinstance(exception, ZeroDivisionError))
    print("Opa, acho que você esqueceu que nao existe divisao por zero")


finally:
    print("Ate logo!")