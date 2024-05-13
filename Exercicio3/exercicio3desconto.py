def calcular_valor_final(valor_produto, percentual_desconto):
    desconto = valor_produto * (percentual_desconto / 100)
    valor_final = valor_produto - desconto
    return valor_final

def main():
    try:
        valor_produto = float(input("Digite o valor do produto: R$ "))
        percentual_desconto = float(input("Digite o percentual de desconto (%): "))
        
        if percentual_desconto < 0 or percentual_desconto > 100:
            print("Percentual de desconto inválido. Deve ser entre 0 e 100.")
            return
        
        valor_final = calcular_valor_final(valor_produto, percentual_desconto)
        print("O valor final após o desconto é: R$", valor_final)

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números.")

if __name__ == "__main__":
    main()
