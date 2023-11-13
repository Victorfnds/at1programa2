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
     print('saindo do programa')
     sys.exit()

# menu de transações
def transacao(tipo):
    if tipo == "compra":
        nome = input(f'nome do produto de {tipo}: ')
        preco = input(f'preço do produto de {tipo}:')
        quantidade = input(f"quantidade do produto de {tipo}")
    if tipo == "venda":
        nome = input(f'nome do produto de {tipo}:')
        preco = input(f'preço do produto de {tipo}:')
        quantidade = input(f"quantidade do produto de {tipo}")
        total = (quantidade(tipo)) * (preco(tipo))
        lucro =  total("compra") - total("venda")
        lista = []
        produto = {tipo, "nome:", nome, "quantidade:", quantidade, "preço:", preco}
        lista.append(produto)
        return (lucro)
