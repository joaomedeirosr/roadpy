class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
 
        if self.__verificarDados(nome, idade):
            self.__realizarCadastro(nome,idade)

        else:
          self.__verificarCadastro()

    def __verificarDados(self, nome: str , idade: int) -> bool:
        if isinstance(nome,str) and isinstance(idade , int):
            return True
        else:
            return False

    def __realizarCadastro(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados, por favor aguarde...')
        print(f'Cadastrar o usuario: {nome}, idade: {idade}')


    def __verificarCadastro(self) -> None:
        print('Ops, os dados digitados sao inválidos por favor, verifique o conteudo digitado')




cadastroUnico = SistemaCadastral()

cadastroUnico.cadastrar('Joao', 26)















# Ou seja se nao seguir os principios SOLID em especifico a Single responsability nosso código 
# possui muitas responsabilidades ferindo os principios do Clean Architecture

#class SistemaCadastral:
    # def cadastrar(self, nome: str, idade: int) -> None:
        # Verificar o formato dos dados
        # if isinstance(nome, str) and isinstance(idade, int):
            # Reponasvel por realizar o cadastro
            # print('Acessando o banco de dados, aguarde...')
            # print(f'Cadastrar o Usuario: {nome}, Idade: {idade}')

        # Responsavel por verificar erros de cadastro
        # else:
            # print('Por favor verifique o que foi digitado')