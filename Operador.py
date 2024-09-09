from Pessoa import Pessoa

class Operador (Pessoa):
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, data_nascimento: str, endereco: str,senha:str,percentualCommissao:float,salario:float):
        super().__init__(nome, cpf, email, telefone, data_nascimento, endereco)
        self.login = False
        self.senha = senha
        self.percentualCommissao = percentualCommissao
        self.salario = salario