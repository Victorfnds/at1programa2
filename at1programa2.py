import sys
print('-' * 20)
print('MENU')
print('-' * 20)
print()
print('OPÇÕES', )
print('[1], - COMPRAS')
print('[2], - VENDAS')
print('[3], - SALDO')
print('[4], - SAIR')
# menu principal
def main(compra, venda):
 while True:
  resposta1 = int(input(" Selecione sua opção:" ))
  if resposta1 ==1:
   main(compra)
  elif resposta1 ==2:
   main(venda)
  elif resposta1 ==3:
   saldo()
  elif resposta1 ==4:
   print('saindo do programa')
   sys.exit()

#definindo variaveis
compra = str
venda = str
#menu de transações
def main():
 print('-' * 20)
 print('MENU')
 print('-' * 20)
 print()
 print('OPÇÕES', )
 print('[1], - NOME')
 print('[2], - QUANTIDADE')
 print('[3], - VALOR')
 print('[4], - SAIR')
resposta = input("insira  a sua opção")
if main() == compra:
 nome = input(f'nome do produto {main()}:')
 preço = input(f'preço do produto {main()}:')
 quantidade = input(f"quantidade do produto {main()}")
 compra.append((nome, preço , quantidade))
if main() == venda:
 nome = input(f'nome do produto {main()}:')
 preço = input(f'preço do produto {main()}:')
 quantidade = input(f"quantidade do produto {main()}")
 venda.append((nome, preço, quantidade))


# criando listas
venda = []
compra = []


#saldo
total = preço(main()) * quantidade(main())


def saldo():
 print("o saldo total é", total(compra) - total(venda))