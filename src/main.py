from src.integrations.ms_teams import connect_to_teams
from src.db.connection import conectar_oracle

def main():
    print("Iniciando o Agente de Reuniões...")
    # Testar conexão com o banco
    conn = conectar_oracle()
    if conn:
        print("Conexão com o banco de dados estabelecida!")
    # Testar integração com Teams
    connect_to_teams()

if __name__ == "__main__":
    main()
