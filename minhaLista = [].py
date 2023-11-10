from socket import SOMAXCONN


def produtos():

    nome = input("nome: ")
    if nome == "sair":
        return False


    preco = int(input("preco:"))
    Lista = []
    produto = {"nome": nome, "preco": preco}
    Lista.append(produto)
    return True

    SOMAXCONN = 0

while produtos():
    pass

for item in Lista:
    SOMAXCONN += item["preço"]

print(Lista)
print(SOMAXCONN)
