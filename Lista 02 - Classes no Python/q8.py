#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2

  def Calcular_media (self):
    media = (self.nota1 + self.nota2) / 2
    return f'A media do Aluno: {self.nome} é {media}'

meu_aluno = str(input('Dígite o nome do aluno: '))
n1 = float(input('Digite a primera nota: '))
n2 = float(input('Digite a segunda nota: '))

nota_aluno = Aluno(meu_aluno, n1, n2)
print(nota_aluno.Calcular_media())