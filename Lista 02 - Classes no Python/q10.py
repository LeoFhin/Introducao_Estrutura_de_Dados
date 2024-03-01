#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 10 - Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
#método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
#do funcionário.

class Funcionario:
  def __init__(self, nome, salario, cargo):
    self.nome = nome
    self. salario = salario
    self.cargo = cargo

  def Aumentar_salario (self, perc_aumento):
    if perc_aumento <= 0:
      print('O valor tem que ser maior que zero!')

    else:
      aumento = self.salario * (perc_aumento / 100)
      self.salario += aumento
      return f'Esse é seu novo salario: {self.salario}'

meu_funcionario = str(input('Digite o nome do funcionario: '))
meu_salario = float(input('Digite o seu salario atual: '))
meu_cargo = str(input('Digite o seu cargo: '))
aumento = float(input('Informe a % do aumento: '))

novo_salario = Funcionario(meu_funcionario, meu_salario, meu_cargo)
print(novo_salario.Aumentar_salario(aumento))