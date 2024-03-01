#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 6 - Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
#método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
  def __init__(self, nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

  def Calcular_total(self):
    self.calcular_total = self.preco * self.quantidade
    return f'O valor total da compra é de: {self.calcular_total}'
meu_produto = str(input('Digite o nome de um produto: '))
o_preco = float(input('Digite o preço do produto: '))
minha_quantidade = int(input('Digite a quantidade desejada: '))

minha_compra = Produto(meu_produto, o_preco, minha_quantidade)
print(f'O produto escolhido foi: {minha_compra.nome}')
print(minha_compra.Calcular_total())