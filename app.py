import streamlit as st
from agent import agent

st.set_page_config(
    page_title="AI stock agent",
    page_icon="🔗"
)

st.header("Bem-Vindo ao Assistente de Estoque")

model_options = [
    'gpt-4.1-nano',
    'gpt-4.1-mini',
    'gpt-4.1',
    'gpt-4o'
]
st.sidebar.image('images/ai_stock_agent.png')

selected_model = st.sidebar.selectbox(
    label='Selecione o modelo LLM',
    options=model_options,
)

st.sidebar.markdown(
    """
    <p style="color:lightgray; font-style:italic;">
        Este agente emprega um modelo GPT avançado para realizar consultas inteligentes em um banco de dados.
    </p>
    """, unsafe_allow_html=True
)

st.write('Faça perguntas sobre o estoque de produtos, preços e reposicões.')
user_question = st.text_input('O que deseja saber sobre o estoque?')

if st.button('Consultar'):
    with st.spinner("Consultando o banco de dados..."):
        if user_question:
            output = agent(selected_model, user_question)
            st.markdown(output.get('output'))
        else:
            st.warning('AGUARDANDO PERGUNTA DO USUÁRIO')
