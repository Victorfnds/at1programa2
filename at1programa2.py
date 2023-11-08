import sys
# menu principal
def main():
 while True:
  print('-' * 20)
  print('MENU')
  print('-' * 20)
  print()
  print('OPÇÕES', )
  print('[C]', - 'COMPRA')
  print('[V]', - 'VENDA')
  print('[S]', - 'SAIR')
resposta = input(" Selecione sua opção:" )
if resposta =="c":
 transacao("compra")
elif resposta =="v":
 transacao("venda")
elif resposta =="s":
 print('saindo do programa')
 sys.exit()

#menu de transações
def transacao(tipo):
  lista = [{"nome:", nome, "quantidade:", quantidade, "preço:", preco}]
   dados.append(lista)

 if tipo == "compra":
  nome = input(f'nome do produto de {tipo}:')
  preco = input(f'preço do produto de {tipo}:')
  quantidade = input(f"quantidade do produto de {tipo}")
  lista.append((tipo, nome, preço , quantidade))
 if tipo == "venda":
  nome = input(f'nome do produto de {tipo}:')
  preco = input(f'preço do produto de {tipo}:')
  quantidade = input(f"quantidade do produto de {tipo}")
  lista.append((tipo, nome, preco, quantidade))
  print("o saldo total é", total("venda") - total("compra"))
  

#saldo
def total(tipo):
  dados = []
 if tipo == "compra":
  preco * quantidade
 elif tipo == "venda":
  preco * quantidade
