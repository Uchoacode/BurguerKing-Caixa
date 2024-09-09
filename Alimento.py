from Produto import *
class Alimento(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)