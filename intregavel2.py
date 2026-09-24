def classificar_cliente(idade, renda):
    if renda >= 10000 and idade >= 30:
        print("Categoria: Diamante")
    elif renda >= 5000:
        print("Categoria: Ouro")
    elif renda >= 2500:
        print("Categoria: Prata")
    else:
        print("Categoria: Bronze")

# Exemplo de uso:
idade_input = int(input("Digite a idade do cliente: "))
renda_input = float(input("Digite a renda do cliente (R$): "))
classificar_cliente(idade_input, renda_input)