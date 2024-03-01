#Aluno: Leonardo santos de lima.
#Turma: P2b
#uniesp: Sistemas para internet

#Questão 01 - Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
#“calcular_area” que retorna a área do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14

    def Calcular_area(self):
        self.area = self.pi * (self.raio * self.raio)

raio_circulo = int(input('Digite o raio do círculo: '))

circulo = Circulo(raio_circulo)
circulo.Calcular_area()
area = circulo.area
print(f'A área do círculo é {area}')