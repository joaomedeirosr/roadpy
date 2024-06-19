class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf


    def correr():
        print('Running!')
    
    def beber(self,bebida):
        if bebida == 'cerveja':
            self.__apresentarDocumento()

        print(f'Bebendo {bebida}...')

    def __apresentarDocumento(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo',30,'365.789.980-80')

ronaldo.beber('Coca-cola')
ronaldo.beber('cerveja')