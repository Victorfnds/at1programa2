# menu principal

import sys

def main():
    while True:
        resposta = input("Selecione sua opção: c para compra, v para venda,l para lucro,s para sair")
        if resposta == "c":
            transacao("compra")
        elif resposta == "v":
            transacao("venda")
        elif resposta == "l":
             lucro()
        elif resposta == "s":
            print('Saindo do programa')
            sys.exit()

# menu de transações
def transacao(tipo):
    lista = []
    if tipo == "compra":
        nome = input(f'Nome do produto de {tipo}: ')
        preco = input(f'preço do produto de {tipo}: ')
        quantidade = input(f'quantidade do produto de{tipo}: ')
        produto_compra = {"nome": nome, "quantidade": quantidade,
                          "preco": preco,}
        lista.append(produto_compra)
    elif tipo == "venda":
        nome = input(f'Nome do produto de {tipo}: ')
        preco = input(f'preco do produto de {tipo}: ')
        quantidade = input(f'quantidade do produto de {tipo}: ')
        produto_venda = {"nome": nome, "quantidade": quantidade,
                         "preco": preco}
        lista.append(produto_venda)

    print(lista)

def lucro():
    # Define quantidade(tipo) and preco(tipo) functions or use appropriate logic here
    total(compra) = quantidade(compra) * preco(compra)
    total(venda) = quantidade(venda) * preco(venda)
    lucro = total("compra") - total("venda")
    return lucro
    print (lucro)

if __name__ == "__main__":
    main()
