#primeiro

# def classificar_cliente(idade, renda):
#     if renda >= 10000 and idade >= 30:
#         print("Categoria: Diamante")
#     elif renda >= 5000:
#         print("Categoria: Ouro")
#     elif renda >= 2500:
#         print("Categoria: Prata")
#     else:
#         print("Categoria: Bronze")

# # Exemplo de uso:
# idade_input = int(input("Digite a idade do cliente: "))
# renda_input = float(input("Digite a renda do cliente (R$): "))
# classificar_cliente(idade_input, renda_input)

#segundo

# def executar_operacao():
#     print("=== MENU DE OPERAÇÕES ===")
#     print("1 - Soma")
#     print("2 - Subtração")
#     print("3 - Multiplicação")
#     print("4 - Divisão")
    
#     opcao = int(input("Escolha uma opção (1-4): "))
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))

#     match opcao:
#         case 1:
#             print(f"Resultado: {num1 + num2}")
#         case 2:
#             print(f"Resultado: {num1 - num2}")
#         case 3:
#             print(f"Resultado: {num1 * num2}")
#         case 4:
#             if num2 != 0:
#                 print(f"Resultado: {num1 / num2}")
#             else:
#                 print("Erro: Divisão por zero não é permitida.")
#         case _:
#             print("Opção inválida!")

# executar_operacao()

#terceiro

# def analisar_numeros():
#     soma = 0.0
#     maior = None
#     menor = None

#     for i in range(1, 6):
#         numero = float(input(f"Digite o {i}º número: "))
#         soma += numero

#         if i == 1:
#             maior = numero
#             menor = numero
#         else:
#             if numero > maior:
#                 maior = numero
#             if numero < menor:
#                 menor = numero

#     media = soma / 5

#     print("\n--- RESULTADOS ---")
#     print(f"Soma: {soma}")
#     print(f"Média: {media}")
#     print(f"Maior número: {maior}")
#     print(f"Menor número: {menor}")

# analisar_numeros()

#quarto

# def sistema_autenticacao():
#     SENHA_CORRETA = "1234"
#     tentativas = 0
#     autenticado = False

#     while tentativas < 3 and not autenticado:
#         senha_digitada = input("Digite a senha: ")
#         tentativas += 1

#         if senha_digitada == SENHA_CORRETA:
#             autenticado = True
#             print("Acesso concedido! Bem-vindo.")
#         else:
#             if tentativas < 3:
#                 print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

#     if not autenticado:
#         print("Acesso bloqueado! Você excedeu o limite de 3 tentativas.")

# sistema_autenticacao()

