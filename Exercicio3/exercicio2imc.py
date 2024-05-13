print("Olá Digite a sua altura e o seu peso")
nome = input("informe seu nome:")

def calcular_imc(peso, altura):
   
    return peso / (altura ** 2)

def classificar_imc(imc):
    
   
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"


peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))


imc = calcular_imc(peso, altura)


tipo = classificar_imc(imc)


print(nome ,"Seu IMC é:", round(imc, 2))
print("Sua classificação é:", tipo)