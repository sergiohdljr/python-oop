class ControleRemoto:
    
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal Avancado')
    
    def voltar_canal(self):
        print('Voltar Canal')

    def escolher_canal(self, canal):
        print('ALterado para o canal: {}'.format(canal))

controle_sala = ControleRemoto('Samsung', 'Sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.voltar_canal()
controle_sala.escolher_canal(15)