from mysql import connector
from datetime import date
import os

HOST = "127.0.0.1"
PORTA = 3306
USUARIO = "root"
SENHA = "admin"
BANCO = "restau_calabresa"

def conectar():
    """Abre a conexão com MySQL e retorna ela"""
    conexao = connector.connect(
        host=HOST,
        port=PORTA,
        user=USUARIO,
        password=SENHA,
        database=BANCO,
    )
    return conexao

def cadastrar():
    print("\n--- CADASTRAR BEBIDAS ---")
    nome = input("Digite o nome da bebida: ")
    valor = float(input("Digite o valor da bebida: ").replace(",", "."))
    tipo = input("Digite o tipo da bebida: ")
    data_vencimento = input("Digite a data de vencimento: ")

    data_vencimento_partes = data_vencimento.split("/")
    data_vencimento = f"{data_vencimento_partes[2]}-{data_vencimento_partes[1]}-{data_vencimento_partes[0]}"

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO bebidas (nome, valor, tipo , data_vencimento) VALUES (%s, %s , %s, %s)",
        (nome, valor , tipo , data_vencimento),
    )

    conexao.commit()
    print(f"\n[OK] bebida cadastrado com id: {cursor.lastrowid}")
    
    cursor.close()
    conexao.close()

def formatar_data(data: date):
    if data is None:
        return "----------"
    # formatar data  no padrão pt-br "22/10/2023"
    return data.strftime("%d/%m/%Y")

def listar_bebidas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT 
            id, nome, valor, tipo, data_vencimento
        FROM bebidas
        ORDER BY nome ASC    
""")

    bebidas = cursor.fetchall()

    if len(bebidas) == 0:
        print("Nenhuma bebida cadastrada")
        return

    
    print("-" * 76, end="")
    print(f"\n{'ID':<4} {'NOME':<25} {'VALOR':<20} {'TIPO':<12} {'DATA DE VENCIMENTO':>12}")
    print("-" * 76)
    for bebida in bebidas:
        id = bebida[0]
        nome = bebida[1]
        valor = bebida[2]
        tipo = bebida[3]
        data_vencimento = formatar_data(bebida[4])

        print(
            f"{id:<4} {nome:<25} {valor:<20} {tipo:<12} {data_vencimento:<12}"
        )
    print("-" * 76)

def excluir_bebida():
    listar_bebidas()

    id_para_apagar = int(input("\nDigite o id para apagar a bebida: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM bebidas WHERE id = %s", (id_para_apagar,)
    )
    conexao.commit()

    conexao.close()
    cursor.close()

    if cursor.rowcount == 0:
        print("Bebida não encontrada com este id")
    else:
        print("Registro apagado com sucesso")

def alterar_bebida():
    listar_bebidas()

    id_para_editar = int(input("Digite o id para editar um registro: "))
    nome = input("Digite o nome da bebida: ")
    valor = float(input("Digite o valor da bebida: ").replace(",", "."))
    tipo = input("Digite o tipo da bebida: ")
    data_vencimento = input("Digite a data de vencimento: ")

    conexao = conectar()
    cursor = conexao.cursor()

    data_vencimento_partes = data_vencimento.split("/")
    data_vencimento = f"{data_vencimento_partes[2]}-{data_vencimento_partes[1]}-{data_vencimento_partes[0]}"


    cursor.execute(
        "UPDATE bebidas SET nome = %s , valor = %s , tipo = %s , data_vencimento = %s WHERE id = %s" ,
        (nome, valor , tipo , data_vencimento , id_para_editar),
    )
    conexao.commit()

    cursor.close()
    conexao.close()

    if cursor.rowcount == 0:
        print("Bebida não encontrada com este id")
    else:
        print("Bebida alterada com sucesso")


def menu_bebidas():

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
            listar_bebidas()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            alterar_bebida()
        elif opcao == 4:
            excluir_bebida()
        elif opcao != 5:
            print("Opção invalida")
        print("\n")

        opcao = int(input(mensagem))
    os.system("clear")