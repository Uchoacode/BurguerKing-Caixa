import uuid

def generate_sku():
    return str(uuid.uuid4()).split("-")[0].upper()

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        self.sku = generate_sku()  # Adiciona o SKU ao produto

    def __str__(self):
        return f'Produto: {self._nome}, Preço: {self._preco}, SKU: {self.sku}'

produto1 = Produto("Batata", 21)
# print(produto1.sku)
