class Pessoa:
    def __init__(self,nome:str,cpf:str,email:str,telefone:str,data_nascimento:str,endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_nascimento = data_nascimento
    

    def comer(self,comida:str):
        return f'{self.nome} está comendo {comida}'