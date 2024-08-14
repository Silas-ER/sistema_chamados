import streamlit as st
import sqlite3

# Função para inserir dados no banco de dados
def atualizar_status(id):
    try:
        # Conectar ao banco de dados
        db = sqlite3.connect('dados_acesso.db')
        cursor = db.cursor()

        # Atualizar o status da solicitação para False
        cursor.execute("""
            UPDATE SOLICITACOES
            SET STATUS = ?
            WHERE ID = ?
        """, (0, id))

        # Confirmar a transação
        db.commit()
        st.success(f"Solicitação {id} fechada com sucesso!")

    except sqlite3.Error as e:
        st.error(f"Erro ao atualizar o status: {e}")

    finally:
        # Fechar a conexão com o banco de dados
        db.close()

def inserir_dados(matricula, nome, telefone, setor, tipo, email, descricao, prioridade, status):
    try:
        # Conectar ao banco de dados
        db = sqlite3.connect('dados_acesso.db')
        cursor = db.cursor()

        # Comando SQL para inserir dados
        cursor.execute("""
            INSERT INTO SOLICITACOES (MATRICULA, NOME, TELEFONE, SETOR, TIPO, EMAIL, DESCRICAO, PRIORIDADE, STATUS)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (matricula, nome, telefone, setor, tipo, email, descricao, prioridade, status))

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