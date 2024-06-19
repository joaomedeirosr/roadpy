class Node:
     def __init__(self, valor , nome_link = None):
         self.valor = valor
         self.nome_link = nome_link

     def get_value(self):
         return self.valor
    
     def set_value(self,valor):
         self.valor = valor
         return valor
    
     def get_nome_link(self):
         return self.nome_link
    
     def set_nome_link(self, nome_link):
         self.nome_link = nome_link
         return nome_link
        
        

numero1 = Node(1,'Eu sou o primeiro')      
numero2 = Node(2,'Eu sou o segundo')      
numero3 = Node(3,'Eu sou o terceiro')


numero1.set_nome_link(numero3)
numero3.set_nome_link(numero2)


 
novo1 = numero1.get_nome_link().get_value()
novo2 = numero3.get_nome_link().get_value()

print(novo1)
print(novo2)
