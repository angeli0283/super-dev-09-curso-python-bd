from banco_dados import conectar
from datetime import date
import os
# pip install mysql-connector-python
# py -m pip install mysql-connector-python

HOST = "127.0.0.1"
PORTA = 3306
USUARIO = "root"
SENHA = "admin"
BANCO = "restau_calabresa"



def cadastrar_prato():
    print("\n----- CADASTRAR PRATO -----")
    nome = input("Digite o nome do prato: ")
    custo = float(input("Digite o valor: ").replace(",", "."))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO pratos_feitos (nome, custo) VALUES (%s, %s)",
        (nome, custo)
    )


    conexao.commit()
    print(f"\n[OK] prato cadastrado com id: {cursor.lastrowid}")

    conexao.close()
    cursor.close()


def listar_pratos():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id, nome, custo FROM pratos_feitos ORDER BY custo ASC"
    )

    pratos = cursor.fetchall()

    if len(pratos) == 0:
        print("Nenhum prato cadastrado")
        return

    print("-"*100, end="")
    print(f"\n{'ID':<4} {'NOME':<25} {'CUSTO':>10}")
    print("-"*100)

    for prato in pratos:
        id = prato[0]
        nome = prato[1]
        custo = prato[2]

        print(
            f"{id:<4} {nome:<25} {custo:>10}"
        )

    print("-"*100)

    conexao.close()
    cursor.close()



def excluir_prato():
    listar_pratos()

    id_deletar = int(input("Digite o id do prato a ser deletado: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pratos_feitos WHERE id = %s", (id_deletar,))
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Prato com esse id não foi encontrado")
    else:
        print("Deletado com sucesso")


def alterar_prato():
    listar_pratos()

    print("\n----- ALTERAR PRATO -----")

    id_alterar = int(input("Digite o id do prato a ser alterado: "))
    nome = input("Digite o nome do prato: ")
    custo = float(input("Digite o valor: ").replace(",", "."))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE pratos_feitos SET nome = %s, custo = %s WHERE id = %s",
        (nome, custo, id_alterar)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Prato com esse id não foi encontrado")
    else:
        print("Prato alterado com sucesso")


def menu_pratos_feitos():

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
            listar_pratos()
        elif opcao == 2:
            cadastrar_prato()
        elif opcao == 3:
            alterar_prato()
        elif opcao == 4:
            excluir_prato()
        elif opcao != 5:
            print("Opção invalida")
        print("\n")

        opcao = int(input(mensagem))
    os.system("clear")