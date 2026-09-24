entregavel 2 portugol
primeiro: 
programa
{
    funcao inicio()
    {
        inteiro idade
        real renda

        escreva("Digite a idade do cliente: ")
        leia(idade)
        escreva("Digite a renda do cliente (R$): ")
        leia(renda)

        se (renda >= 10000 e idade >= 30)
        {
            escreva("Categoria: Diamante\n")
        }
        senao se (renda >= 5000)
        {
            escreva("Categoria: Ouro\n")
        }
        senao se (renda >= 2500)
        {
            escreva("Categoria: Prata\n")
        }
        senao
        {
            escreva("Categoria: Bronze\n")
        }
    }
}

segundo:
programa
{
    funcao inicio()
    {
        inteiro opcao
        real num1, num2, resultado

        escreva("=== MENU DE OPERAÇÕES ===\n")
        escreva("1 - Soma\n")
        escreva("2 - Subtração\n")
        escreva("3 - Multiplicação\n")
        escreva("4 - Divisão\n")
        escreva("Escolha uma opção (1-4): ")
        leia(opcao)

        escreva("Digite o primeiro número: ")
        leia(num1)
        escreva("Digite o segundo número: ")
        leia(num2)

        escolha (opcao)
        {
            caso 1:
                resultado = num1 + num2
                escreva("Resultado: ", resultado, "\n")
                pare
            caso 2:
                resultado = num1 - num2
                escreva("Resultado: ", resultado, "\n")
                pare
            caso 3:
                resultado = num1 * num2
                escreva("Resultado: ", resultado, "\n")
                pare
            caso 4:
                se (num2 != 0)
                {
                    resultado = num1 / num2
                    escreva("Resultado: ", resultado, "\n")
                }
                senao
                {
                    escreva("Erro: Divisão por zero não é permitida.\n")
                }
                pare
            caso contrario:
                escreva("Opção inválida!\n")
        }
    }
}

terceiro:

programa
{
    funcao inicio()
    {
        real numero, soma = 0.0, media, maior = 0.0, menor = 0.0
        inteiro i

        para (i = 1; i <= 5; i++)
        {
            escreva("Digite o ", i, "º número: ")
            leia(numero)

            soma = soma + numero

            se (i == 1)
            {
                maior = numero
                menor = numero
            }
            senao
            {
                se (numero > maior)
                {
                    maior = numero
                }
                se (numero < menor)
                {
                    menor = numero
                }
            }
        }

        media = soma / 5

        escreva("\n--- RESULTADOS ---\n")
        escreva("Soma: ", soma, "\n")
        escreva("Média: ", media, "\n")
        escreva("Maior número: ", maior, "\n")
        escreva("Menor número: ", menor, "\n")
    }
}

quarto:

programa
{
    funcao inicio()
    {
        cadeia senha_correta = "1234"
        cadeia senha_digitada
        inteiro tentativas = 0
        logico autenticado = falso

        enquanto (tentativas < 3 e nao autenticado)
        {
            escreva("Digite a senha: ")
            leia(senha_digitada)
            tentativas = tentativas + 1

            se (senha_digitada == senha_correta)
            {
                autenticado = verdadeiro
                escreva("Acesso concedido! Bem-vindo.\n")
            }
            senao
            {
                se (tentativas < 3)
                {
                    escreva("Senha incorreta. Tentativas restantes: ", 3 - tentativas, "\n")
                }
            }
        }

        se (nao autenticado)
        {
            escreva("Acesso bloqueado! Você excedeu o limite de 3 tentativas.\n")
        }
    }
}
