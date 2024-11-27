import psycopg2
from src.config.settings import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def criar_tabelas():
    """Cria a estrutura do banco de dados no PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Conexão com o banco de dados bem-sucedida!")

        with conn.cursor() as cursor:
            print("Criando tabelas...")

            # Tabela de Reuniões
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS reunioes (
                id_reuniao SERIAL PRIMARY KEY,
                titulo VARCHAR(200) NOT NULL,
                data_hora_inicio TIMESTAMP NOT NULL,
                data_hora_fim TIMESTAMP,
                organizador VARCHAR(100),
                participantes JSONB
            );
            """)

            # Tabela de Transcrições
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transcricoes (
                id_transcricao SERIAL PRIMARY KEY,
                id_reuniao INTEGER NOT NULL,
                falante VARCHAR(100),
                texto TEXT,
                data_hora_fala TIMESTAMP,
                CONSTRAINT fk_reuniao FOREIGN KEY (id_reuniao) REFERENCES reunioes(id_reuniao)
            );
            """)

            conn.commit()
            print("Estrutura do banco de dados criada com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao criar tabelas: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    criar_tabelas()
