class Calculadora:

    def calcular (self, operacao: str, num1: float, num2: float) -> int:
        if operacao  == '+':
            return self.__adicionar(num1,num2)
        elif operacao == '-':
            return self.__subtrair(num1,num2)
        else:
            print("Operacao invalida")
        

    def __adicionar(self, num1, num2) -> int:
        soma = num1 + num2
        return print(soma)

    def __subtrair(self, num1, num2) -> int:
        subtracao = num1 - num2
        return print(subtracao)
    

calculando = Calculadora()
somar = calculando.calcular('+' , 3, 5)
subtrair = calculando.calcular('-', 5 , 3)
