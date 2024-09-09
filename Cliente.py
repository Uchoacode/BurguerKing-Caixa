from Pessoa import Pessoa


class Cliente (Pessoa):
    
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, data_nascimento: str, endereco: str,cupom:str):
        super().__init__(nome, cpf, email, telefone, data_nascimento, endereco)
        self.cupom = cupom
        self.pontuacao = 0

        # def comprar(self,)
