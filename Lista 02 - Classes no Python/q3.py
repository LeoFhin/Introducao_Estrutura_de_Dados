#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 3 - Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
#chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    self.area = self.base * self.altura
    return f'O valor da área do retangulo é: {self.area}'

valor_base = int(input('Dígite a base do rentagulo: '))
valor_altura = int(input('Dígite a altura do retangulo: '))

meu_retangulo = Retangulo(valor_base, valor_altura)
print(meu_retangulo.calcular_area())