class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        self.__estado = valor

    

policia = Alarme(False)
policia_alarme_on = policia.set_estado(True)
policia_alarme_on = policia.get_estado() 
print(policia_alarme_on)


        
