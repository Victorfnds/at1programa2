# menu principal

import sys


def main():
    while True:
        resposta = input(" Selecione sua opção:c para compra,v para venda,s para sair")
        if resposta == "c":
            transacao("compra")
        elif resposta == "v":
            transacao("venda")
        elif resposta == "s":
            print("saindo do programa")
            sys.exit()




def transacao(tipo):
 if tipo == "compra":
    nome_compra = input("digite o nome do produto: ").split()
    nome_compra = list(nome_compra)
    preco_compra = input("Digite o preço de compra: ").split()
    preco_compra = list(preco_compra)
    quant_compra = input("digite a quantidade: ").split()
    quant_compra = list(quant_compra)

 if tipo == "venda":
    nome_venda = input("digite o nome do produto: ").split()
    nome_venda = list(nome_venda)
    preco_venda = input("Digite o preço de venda: ").split()
    preco_venda = list(preco_venda)
    quant_venda = input("digite a quantidade: ").split()
    quant_venda = list(quant_venda)


# criando lista
lista_relatorio_financeiro = list[
    "nome_compra",
    "preco_compra",
    "quant_compra",
    "nome_venda",
    "preco_venda",
    "quant_venda",
    "total_compra",
    "total_venda",
]
# total de compras e vendas
total_compra = preco_compra * quant_compra
total_venda = preco_venda * quant_venda

# Calculando o lucro líquido
lucro = ("total_venda") - ("total_compra")

# Imprimindo o resultado
print("O lucro líquido é de R${:.2f}".format(lucro))
