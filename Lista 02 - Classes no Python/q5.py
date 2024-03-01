#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 5 - Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
#chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def falar (self, fala):
    self.fala = fala
    return f'{fala}'

meu_nome = str(input('Digite o seu nome: '))
minha_idade = int(input('Dígite a sua idade: '))
minha_fala = str(input('Digite uma fala:' ))

minha_pessoa = Pessoa(meu_nome, minha_idade)
minha_pessoa.falar(minha_fala)
print(f'Me chamo {minha_pessoa.nome} \n Gostaria de dizer: {minha_pessoa.fala}')