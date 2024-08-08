import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
db = sqlite3.connect('dados_acesso.db')

# Criar um cursor para executar comandos SQL
cursor = db.cursor()

# Criar a tabela SOLICITACOES
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS SOLICITACOES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        MATRICULA INTEGER NOT NULL,
        NOME TEXT NOT NULL,
        TELEFONE TEXT NOT NULL,
        SETOR TEXT NOT NULL,
        TIPO TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        DESCRICAO TEXT NOT NULL
    )
    """
)

print("Tabela SOLICITACOES criada com sucesso!")

# Confirmar as alterações no banco de dados
db.commit()

# Fechar a conexão com o banco de dados
db.close()

