#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 9 - Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
#método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
  def __init__(self, lado1, lado2, lado3):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3

  def Calcular_perimetro(self):
    perimetro =  self.lado1 + self.lado2 + self.lado3
    return f'O perímetro do triângulo é {perimetro}'

l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))

meu_triangulo = Triangulo(l1, l2, l3)
print(meu_triangulo.Calcular_perimetro())