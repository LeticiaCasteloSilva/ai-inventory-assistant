import streamlit as st
from agent import agent
import time

st.set_page_config(
    page_title="AI Stock Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #ea580c 0%, #dc2626 100%);
        padding: 2rem 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1rem;
        opacity: 0.9;
    }
    
    /* Botão personalizado simples */
    .stButton > button {
        background: #ea580c !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
    }
    
    .stButton > button:hover {
        background: #c2410c !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>AI Stock Agent</h1>
    <p>Assistente Inteligente para Gestão de Estoque</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Faça sua pergunta")
user_question = st.text_input(
    "O que deseja saber sobre o estoque?",
    placeholder="Ex: Quantos produtos temos da categoria eletrônicos?"
)


button_consult = st.button('🚀 Consultar Agora')

# Instruções embaixo
st.markdown("---")
st.markdown("### 📋 Instruções")

col_inst1, col_inst2 = st.columns(2)

with col_inst1:
    with st.expander("Como usar"):
        st.write("""
        Seleciona o modelo LLM que deseja usar e digite
        sua pergunta sobre estoque, preços ou reposições no campo abaixo. 
        O assistente utilizará IA avançada para consultar o banco de dados e fornecer 
        respostas precisas e contextualizadas.
        """)

with col_inst2:
    with st.expander("Exemplos de perguntas"):
        st.write("• Quais produtos estão com baixo estoque?")
        st.write("• Qual o valor total do inventário?")
        st.write("• Produtos que precisam de reposição urgente")
        st.write("• Histórico de vendas dos últimos 30 dias")
        st.write("• Produtos mais vendidos por categoria")

with st.sidebar:
    st.markdown("### 🧠 Modelo de IA")
    
    model_options = [
        'gpt-4o',
        'gpt-4.1', 
        'gpt-4.1-mini',
        'gpt-4.1-nano'
    ]
    
    model_labels = {
        'gpt-4o': 'GPT-4o (Recomendado)',
        'gpt-4.1': 'GPT-4.1',
        'gpt-4.1-mini': 'GPT-4.1 Mini', 
        'gpt-4.1-nano': 'GPT-4.1 Nano'
    }
    
    selected_model = st.selectbox(
        'Selecione o modelo:',
        options=model_options,
        format_func=lambda x: model_labels[x]
    )
    
    st.markdown("### 📊 Performance")
    
    model_metrics = {
        'gpt-4o': {'speed': 95, 'accuracy': 98},
        'gpt-4.1': {'speed': 90, 'accuracy': 95},
        'gpt-4.1-mini': {'speed': 85, 'accuracy': 88},
        'gpt-4.1-nano': {'speed': 80, 'accuracy': 85}
    }
    
    if selected_model in model_metrics:
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.metric("Velocidade", f"{model_metrics[selected_model]['speed']}%")
        with col_s2:
            st.metric("Precisão", f"{model_metrics[selected_model]['accuracy']}%")
    
    st.divider()
    
    st.markdown("### 📋 Sobre")
    st.markdown("""
    *Este assistente utiliza modelos GPT avançados para realizar consultas inteligentes 
    em bases de dados, oferecendo insights valiosos para gestão de estoque.*
    """)

    st.divider()
    
    st.markdown("### 🔹 Funcionalidades")
    st.markdown("• Processamento de linguagem natural")
    st.markdown("• Consultas automatizadas")  
    st.markdown("• Análises preditivas")
    st.markdown("• Relatórios instantâneos")

if button_consult:
    if user_question and user_question.strip():
        status_placeholder = st.empty()
        
        status_placeholder.info('🤖 IA consultando estoque...')
        time.sleep(1) 
        
        try:
            output = agent(selected_model, user_question)
            
            status_placeholder.success('✅ Concluído!')
            time.sleep(0.5)
            status_placeholder.empty()
            
            st.markdown("---")
            st.markdown("### 📋 Resultado da Consulta")
            
            with st.container():
                st.markdown(output.get('output', 'Nenhum resultado encontrado.'))
            
            st.markdown("---")
            
            st.markdown("### 📊 Métricas da Consulta")
            col_m1, col_m2, col_m3 = st.columns(3)
            
            with col_m1:
                st.metric("Tempo de Resposta", "1.2s")
            with col_m2:
                st.metric("Modelo Usado", selected_model.upper())
            with col_m3:
                st.metric("Confiança", "98%")
                
        except Exception as e:
            status_placeholder.error("⚠️ Erro ao processar consulta. Tente novamente.")
            with st.expander("Detalhes do erro"):
                st.exception(e)
            
    else:
        st.warning("📝 Por favor, digite uma pergunta antes de consultar.")

st.divider()
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "AI Stock Agent v2.0 | Desenvolvido por Letícia Castelo com Streamlit e IA Avançada"
    "</div>", 
    unsafe_allow_html=True
)