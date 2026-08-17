from mysql import connector
import os

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

def cadastrar():
    print("\n--- CADASTRAR MESA ---")
    numero = input("Digite o numero da mesa: ")
    lugares = int(input("Digite o total de lugares nessa mesa: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO mesas (numero, lugares) VALUES (%s, %s)",
        (numero , lugares),
    )

    conexao.commit()
    print(F"\n [OK] Mesa cadastrada como id: {cursor.lastrowid}")

    conexao.close()
    cursor.close()

def listar_mesas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id, numero, lugares
        FROM mesas
        ORDER BY numero ASC
        """
    )

    mesas = cursor.fetchall()

    if len(mesas) == 0:
        print("nenhuma mesa foi cadastrada:")
        return

    print("-" * 76, end="")
    print(f"\n{'ID':<4} {'NUMERO':<25} {'LUGARES':<20}")
    print("-" * 76, end="")
    for mesa in mesas:
        id = mesa[0]
        numero = mesa[1]
        lugares = mesa[2]

        print(
            f"\n{id:<4} {numero:<25} {lugares:<20}"
        )

    print("-" * 76, end="")

    conexao.close()
    cursor.close()

def excluir_mesa():
    listar_mesas()

    id_mesa_para_apagar = int(input("\n Digite o id da mesa que deseja apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM mesas where id = %s", (id_mesa_para_apagar,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Mesa não encontrado com este id")
    else:
        print("Registro apagado com sucesso")

def alterar_mesas():
    listar_mesas()

    conexao = conectar()
    cursor = conexao.cursor()

    id_mesa_updade = int(input("\n Digite o id da mesa que deseja alterar: "))
    numero_mesa = input("Qual será o numero a mesa? ")
    lugares_mesa = int(input("Quantos lugares ele terá? "))

    cursor.execute(
        "UPDATE mesas SET numero = %s, lugares = %s WHERE id = %s", 
        (numero_mesa , lugares_mesa , id_mesa_updade, ),
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Mesa não encontrado com este id")
    else:
        print("Mesa alterado com sucesso")

    

def menu_mesas():

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
            listar_mesas()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_mesas()
        elif opcao == 4:
            excluir_mesa()
        elif opcao != 5:
            print("Opção invalida")
        print("\n")

        opcao = int(input(mensagem))
    os.system("clear")