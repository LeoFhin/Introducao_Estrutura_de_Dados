#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 2 - Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
#chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def detalhes(self):
    return f'O nome do Livro é: {self.titulo}\nO nome do autor é: {self.autor}'

nome_titulo = str(input('Dígite o nome do livro: '))
nome_autor = str(input('Dígite o nome do autor: '))

meu_livro = Livro(nome_titulo, nome_autor)
print(meu_livro.detalhes())