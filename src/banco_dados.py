from dotev import load_dotenv
from mysql import connector
import os

# Carregar variáveis de ambiente as variaveis definidas no arquivo .env
load_dotenv()

HOST = os.getenv("BD_HOST")
PORTA = os.getenv("BD_PORTA")
USUARIO = os.getenv("BD_USUARIO")
SENHA = os.getenv("BD_SENHA")
BANCO = os.getenv("BD_NOME")

def connectar():
    """Abre a conexão com MySQL e retorna ela"""
    conexao = connector.connect(
        host=HOST,
        port=PORTA,
        user=USUARIO,
        password=SENHA,
        database=BANCO,
    )
    return conexao