import streamlit as st
from inserts import inserir_dados

col1, col2, col3 = st.columns([0.5, 2, 0.5])

status = True
with col1:
    pass

with col2:
    # Iniciando um formulário
    with st.form(key="formulario"):
        # Usando colunas dentro do formulário
        col2_1, col2_2 = st.columns(2)

        with col2_1:

            name_input = st.text_input(
                "Nome:",
                label_visibility="visible",
                disabled=False,
                placeholder="Digite seu nome aqui",
                key="nome"
            )

            setor_option = st.selectbox(
                "Setor:",
                ("Corregedoria", "Auditoria", "UIAG", "Financeiro"),
                label_visibility="visible",
                disabled=False,
                key="setor"
            )

            matricula_input = st.text_input(
                "Matricula:",
                label_visibility="visible",
                disabled=False,
                placeholder="Digite sua matricula aqui",
                key="matricula"
            )

        email_input = st.text_input(
            "Email:",
            label_visibility="visible",
            disabled=False,
            placeholder="Digite seu email aqui",
            key="email"
        )

        with col2_2:

            telefone_input = st.text_input(
                "Telefone:",
                label_visibility="visible",
                disabled=False,
                placeholder="Digite seu telefone aqui",
                key="telefone"
            )

            tipo_option = st.selectbox(
                "Tipo de problema:",
                ("Hardware", "Software"),
                label_visibility="visible",
                disabled=False,
                key="tipo"
            )
            
            prioridade = st.selectbox(
                "Prioridade:",
                ("Alta", "Baixa", "Intermediaria"),
                label_visibility="visible",
                disabled=False,
                key="prioridade"
            )

        # Botão de submissão dentro do formulário
        txt = st.text_area(
            "Descrição:",
            placeholder="Descreva mais destalhes do seu problema!",
        )

        submit_button = st.form_submit_button(
            label="Enviar",
            type="secondary",
            use_container_width=True 
        )

        # Ações a serem tomadas após o envio do formulário
        if submit_button:
            inserir_dados(matricula_input, name_input, telefone_input, setor_option, tipo_option, email_input, txt, prioridade, status)    
with col3:
    pass
