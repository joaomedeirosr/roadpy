class ControleRemoto:
    
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
    
    def avancarCanal(self):
        print(f'{self.televisao} avancou o canal')

    def voltaCanal(self):
        print(f'{self.televisao} voltou o canal')

    def escolherCanal(self, canal):
        self.canal = canal 
        print(f'Voce escolheu o canal {canal}')
        


tv_nova = ControleRemoto('Apple TV','Sala principal')



tv_nova.avancarCanal()
tv_nova.voltaCanal()
tv_nova.escolherCanal(80)


