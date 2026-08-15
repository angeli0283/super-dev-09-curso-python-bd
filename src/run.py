from funcionario import alterar_funcionario, menu_funcionario


def __main():
    alterar_funcionario()
    #excluir_funcionario()
    #listar_funconarios()
    ##print("abrindo conexão com o banco de dados")
    ##conexao= conectar()
    #print("Conexão aberta com sucesso")

    mensagem = """MENU:
1- Funcionários
2 - Pratos feitos
3 - Clientes
4 - Bebidas
5 - Mesas
10- Sair
Digite a opção desejada: """

    opcao = int(input(mensagem))
    
    while opcao != 10:
        if opcao == 1:
            menu_funcionario()
        elif opcao != 10:
            print("Opção inválida")
        print("\n")
    
        opcao = int(input(mensagem))

    
if __name__== "__main__":
    __main()