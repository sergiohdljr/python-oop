class Pessoa:  # substantivo

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome  # substantivo
        self.idade = idade  # substantivo

    def dirigir(self, veiculo: str) -> None:  # Verbos
        print('Dirigindo uma(a) {}'.format(veiculo))

    def cantar(self) -> None:  # Verbos
        print('Lalalalala')

    def apresentar_idade(self) -> int:  # Verbos
        return self.idade
