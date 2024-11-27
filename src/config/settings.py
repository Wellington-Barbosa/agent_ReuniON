import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Banco de Dados PostgreSQL
DB_HOST = os.getenv("DB_HOST", 'localhost')
DB_PORT = os.getenv("DB_PORT", 5432)  # Porta padrão do PostgreSQL
DB_NAME = os.getenv("DB_NAME", 'bot_reunion')
DB_USER = os.getenv("DB_USER", 'wellington')
DB_PASSWORD = os.getenv("DB_PASSWORD", 'Euamominhamae775#')

# Configurações da Microsoft Graph API
MS_CLIENT_ID = os.getenv("MS_CLIENT_ID")
MS_CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET")
MS_TENANT_ID = os.getenv("MS_TENANT_ID")
