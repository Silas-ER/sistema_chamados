import streamlit as st
import pandas as pd
from inserts import select
import plotly.graph_objects as go
from inserts import atualizar_status
import time

st.set_page_config(layout="wide")

dados = select()

# Criando um DataFrame a partir dos dados lidos
colunas = ["ID", "MATRICULA", "NOME", "TELEFONE", "SETOR", "TIPO", "EMAIL", "DESCRICAO", "STATUS"]
df = pd.DataFrame(dados, columns=colunas)

# Exibindo os dados em uma tabela no Streamlit
st.title("Dashboard de Solicitações")
st.write("Abaixo estão os dados das solicitações armazenadas:")

if not df.empty:
    # Contadores
    count_solicitacoes = df['SETOR'].value_counts()
    count_tipos = df['TIPO'].value_counts()

    # Converter
    df_count = count_solicitacoes.reset_index()
    df_count_tipo = count_tipos.reset_index()

    df_count.columns = ['SETOR', 'COUNT']
    df_count_tipo.columns = ['TIPO', 'COUNT']

    # Exibição
    col1, col2 = st.columns(2)
    
    with col1:
        fig_bar = go.Figure(data=[go.Bar(x=df_count['SETOR'], y=df_count['COUNT'])])
        fig_bar.update_layout(title="Solicitações por Setor",
                              xaxis_title="Setor",
                              yaxis_title="Quantidade",
                              template="plotly_white")
        st.plotly_chart(fig_bar)



    with col2:
        # Criando o gráfico de pizza com Plotly Graph Objects
        grafico_pesca_tipo = go.Figure(go.Pie(labels=df_count_tipo['TIPO'],
                                    values=df_count_tipo['COUNT'],
                                    hoverinfo='none',  # Desativar o hoverinfo padrão
                                    hovertemplate='<b>%{label}</b><br>Quantidade: %{value}<extra></extra>'
                                ))

        # Adicionando título ao gráfico
        grafico_pesca_tipo.update_layout(title_text='Solicitações no Período', showlegend=True, legend_title='Tipo de solicitação:')

        st.plotly_chart(grafico_pesca_tipo)


    df_true_status = df[df["STATUS"] == True]
    if not df_true_status.empty:
        with st.container():
                st.title("Solicitações em aberto:")
                st.write("----")
                for row in df_true_status.itertuples():
                    col1, col2 = st.columns([4, 1])

                    with col1:
                        st.write(f"""
                                Nova Solicitação do tipo {row.TIPO}: {row.NOME} do setor {row.SETOR}, relata {row.DESCRICAO}, com os seguintes dados de contato: {row.TELEFONE} e {row.EMAIL}
                                """, unsafe_allow_html=True)
                    
                    with col2:
                        if st.button(f"Fechar Solicitação {row.ID}", key=row.ID):
                            atualizar_status(row.ID)
                            time.sleep(4)
                            st.rerun()

                    st.write("----")
    else:
        st.write("Não há registros com STATUS igual a True.")
        
else:
    st.write("Nenhum dado encontrado.")
