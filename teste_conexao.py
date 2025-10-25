from sqlalchemy import create_engine

# 🔧 Substitua pelos seus dados do MySQL
USUARIO = "root"        # ou outro usuário que você usa
SENHA = "1234"          # coloque sua senha
HOST = "localhost"
BANCO = "estoque"       # nome do seu banco de dados

# 🔗 Monta a string de conexão
url_conexao = f"mysql://{USUARIO}:{SENHA}@{HOST}/{BANCO}"

try:
    print("⏳ Tentando conectar ao banco de dados...")
    engine = create_engine(url_conexao)
    conexao = engine.connect()
    print("✅ Conexão bem-sucedida com o banco de dados MySQL!")
    conexao.close()
except Exception as e:
    print("❌ Erro ao conectar:")
    print(e)
