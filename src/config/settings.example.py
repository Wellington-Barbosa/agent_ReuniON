import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Banco de Dados PostgreSQL
DB_HOST = os.getenv("DB_HOST", 'localhost')
DB_PORT = os.getenv("DB_PORT", 5432)  # Porta padrão do PostgreSQL
DB_NAME = os.getenv("DB_NAME", 'banco_default')
DB_USER = os.getenv("DB_USER", 'usuario_default')
DB_PASSWORD = os.getenv("DB_PASSWORD", 'senha_default')

# Configurações da Microsoft Graph API
MS_CLIENT_ID = os.getenv("MS_CLIENT_ID", 'your_client_id_here')
MS_CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET", 'your_client_secret_here')
MS_TENANT_ID = os.getenv("MS_TENANT_ID", 'your_tenant_id_here')
