#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

class Carro:
  def __init__ (self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def detalhes (self):

    return f'A marca do seu carro: {self.marca} \n O modelo: {self.modelo} \n O ano: {self.ano}'

minha_marca = str(input('Dígite a marca: '))
meu_modelo = str(input('Dígite o modelo: '))
o_ano = int(input('Dígite a ano: '))

meu_carro = Carro(minha_marca, meu_modelo, o_ano)
print(meu_carro.detalhes())