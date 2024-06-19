class Urso:

    def __init__(self,color):
        self.ursinho = 'O urso é grande!'
        self.cor = color

    def dormir(self):
        print('Estou dormindo!!')

    def diasDormidos(self,tempo,mult):
        return tempo * mult

urso_dorminhoco = Urso(color='Brown')

# Atributos , caracteristicas ou variaveis no contexto de uma classe
bear_color = urso_dorminhoco.cor
print(bear_color)

big_bear = urso_dorminhoco.ursinho
print(big_bear)


# Métodos!
urso_dorminhoco.dormir()
nap = urso_dorminhoco.diasDormidos(2,5)
print(f'O urso dorminhoco dormiu {nap} dias')

    

