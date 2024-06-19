class Pessoa:
    def __init__(self, name: str, idade: int ) -> None:
        self.name = name
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print(f'Dirigindo um {veiculo}')

    def canta(self) -> None:
        print('Lalalalal')

    def apresentar_idade(self) -> int:
        return self.idade


maiorzim = Pessoa('Motoboy 2K', 24)

