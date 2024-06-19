class MinhaClasse:

    estaticon = 'lhama'

    def __init__(self,estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Programador'

obj1 = MinhaClasse('aaa')
obj2 = MinhaClasse('aaa')

obj1.mudar_estatico()


obj1.print_estatico()
obj2.print_estatico()

