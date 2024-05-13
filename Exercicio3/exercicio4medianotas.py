#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#Para calcular a media de tres valores indicados pelo usuario



print("Calculando a media de notas\n")

print('Digite as notas do aluno para calcular a media.\n')

nome = input("digite o nome do aluno:")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = ((nota1 + nota2 + nota3)/3)
print("A media do aluno", nome, 'é', media)