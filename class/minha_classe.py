class MinhaClass:
    
    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo'
        self.meu_atributo2 = att

    def meu_metodo(self):
        print(self.meu_atributo)
        print(self.meu_atributo2)
    
    def  meu_metodo2(self, num, mult):
        return num * mult



objeto = MinhaClass('meu atributo')
objeto.meu_metodo()