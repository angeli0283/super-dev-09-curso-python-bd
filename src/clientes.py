from mysql import connector
from datetime import date
import os
# pip install mysql-connector-python
# py -m pip install mysql-connector-python

HOST = "127.0.0.1"
PORTA = 3306
USUARIO = "root"
SENHA = "admin"
BANCO = "restau_calabresa"


def conectar():
    conexao = connector.connect(
        host=HOST,
        port=PORTA,
        user=USUARIO,
        password=SENHA,
        database=BANCO,
    )
    return conexao


def cadastrar_cliente():
    print("\n----- CADASTRAR CLIENTE -----")
    nome = input("Digite o nome do cliente: ")
    documento = input("Digite o documento: ")
    telefone = input("digite o Telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO clientes (nome, documento, telefone) VALUES (%s, %s, %s)",
        (nome, documento, telefone)
    )


    conexao.commit()
    print(f"\n[OK] cliente cadastrado com id: {cursor.lastrowid}")

    conexao.close()
    cursor.close()


def listar_clientes():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, documento, telefone FROM clientes ORDER BY nome ASC"
    )

    clientes = cursor.fetchall()

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
        return

    print("-"*100, end="")
    print(f"\n{'ID':<4} {'NOME':<25} {'DOCUMENTO':<20} {'TELEFONE':<20}")
    print("-"*100)

    for cliente in clientes:
        id = cliente[0]
        nome = cliente[1]
        documento = cliente[2]
        telefone = cliente[3]

        print(
            f"{id:<4} {nome:<25} {documento:<20} {telefone:<20}"
        )

    print("-"*100)

    conexao.close()
    cursor.close()


def excluir_cliente():
    listar_clientes()

    id_deletar = int(input("Digite o id do cliente a ser deletado: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_deletar,))
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Cliente com esse id não foi encontrado")
    else:
        print("Deletado com sucesso")


def alterar_cliente():
    listar_clientes()

    print("\n----- ALTERAR CLIENTE -----")

    id_alterar = int(input("Digite o id do cliente a ser alterado: "))
    nome = input("Digite o nome do cliente: ")
    documento = input("Digite o documento: ")
    telefone = input("Digite o telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE clientes SET nome = %s, documento = %s, telefone = %s WHERE id = %s",
        (nome, documento, telefone, id_alterar)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Cliente com esse id não foi encontrado")
    else:
        print("Cliente alterado com sucesso")


def menu_clientes():

    mensagem = """MENU:
1 - Listar
2 - Cadastrar
3 - Editar
4 - Apagar
5 - Sair

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao != 5:
        os.system("clear")

        if opcao == 1:
            listar_clientes()
        elif opcao == 2:
            cadastrar_cliente()
        elif opcao == 3:
            alterar_cliente()
        elif opcao == 4:
            excluir_cliente()
        elif opcao != 5:
            print("Opção invalida")
        print("\n")

        opcao = int(input(mensagem))
    os.system("clear")