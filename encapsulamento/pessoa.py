class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        # atributo privado
        self.__cpf = cpf

    # encapsulamento privado: acesso apenas pela classe 
    def __apresentar_documento(self):
        print(self.__cpf)

    def beber(self, bebida):
        if bebida == 'cerveja':
           self.__apresentar_documento()
        print('bebendo...')
        
    #encapsulamento público
    def correr (self):
        print('estou correndo')

  
ronaldo = Pessoa('Ronaldo', 32, '708.859.194-40')
print(ronaldo.nome, ronaldo.idade)
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')