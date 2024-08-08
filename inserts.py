import streamlit as st
import sqlite3

# Função para inserir dados no banco de dados
def inserir_dados(matricula, nome, telefone, setor, tipo, email, descricao):
    try:
        # Conectar ao banco de dados
        db = sqlite3.connect('dados_acesso.db')
        cursor = db.cursor()

        # Comando SQL para inserir dados
        cursor.execute("""
            INSERT INTO SOLICITACOES (MATRICULA, NOME, TELEFONE, SETOR, TIPO, EMAIL, DESCRICAO)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (matricula, nome, telefone, setor, tipo, email, descricao))

        # Confirmar a transação
        db.commit()
        st.success("Dados inseridos com sucesso!")

    except sqlite3.Error as e:
        st.error(f"Erro ao inserir os dados: {e}")

    finally:
        # Fechar a conexão com o banco de dados
        db.close()

def select():
    try:
        # Conectar ao banco de dados
        db = sqlite3.connect('dados_acesso.db')
        cursor = db.cursor()

        # Executar uma consulta para selecionar todos os dados da tabela
        cursor.execute("SELECT * FROM SOLICITACOES")
        dados = cursor.fetchall()

        return dados

    except sqlite3.Error as e:
        st.error(f"Erro ao ler os dados: {e}")
        return []

    finally:
        # Fechar a conexão com o banco de dados
        db.close()