entregavel 2 primeiro exercicio:
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
