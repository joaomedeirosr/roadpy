class Calculadora:

    def calcular(self, op , num1,num2):
        if op == '+':
            return self.__adicionar(num1,num2)
        elif op == '-':
            return self.__subtrair(num1,num2)
        else:
            print("Operacao Inválida")
    
    def __adicionar(self,num1,num2):
        soma = num1 + num2
        return print(soma)
    
    def __subtrair(self,num1, num2):
        subtracao = num1 - num2
        return print(subtracao)


calculadora_maluca = Calculadora()

somando = calculadora_maluca.calcular('+', 3 , 5)
subtraindo = calculadora_maluca.calcular('-',12,6)