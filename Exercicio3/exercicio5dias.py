#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#calculo de dias


dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))

total = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Convertido em segundos é igual a %10d segundos." % total)