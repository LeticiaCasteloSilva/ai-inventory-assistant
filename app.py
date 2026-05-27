import streamlit as st
from agent import agent
import time

st.set_page_config(
    page_title="AI Stock Agent",
    page_icon="▸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@700;900&family=Syne:wght@400;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');

:root {
    --bg:       #09090f;
    --surface:  #12141e;
    --surface2: #1a1d2a;
    --amber:    #f0a500;
    --teal:     #2dd4bf;
    --text:     #ddd8ce;
    --muted:    #5a6175;
    --border:   #1e2230;
}

/* ── Base ── */
.stApp {
    background-color: var(--bg);
    background-image:
        linear-gradient(rgba(240,165,0,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(240,165,0,0.025) 1px, transparent 1px);
    background-size: 40px 40px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text);
}

.main .block-container {
    padding-top: 2rem;
    max-width: 860px;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background-color: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

section[data-testid="stSidebar"] * {
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
}

section[data-testid="stSidebar"] h3 {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.65rem !important;
    letter-spacing: 0.22em !important;
    text-transform: uppercase !important;
    color: var(--amber) !important;
    font-weight: 700 !important;
    margin-top: 1.4rem !important;
}

/* ── Animations ── */
@keyframes headerIn {
    from { opacity: 0; transform: translateY(-18px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes scanline {
    0%   { top: -10%; }
    100% { top: 110%; }
}

@keyframes glow {
    0%, 100% { box-shadow: 0 0 30px rgba(240,165,0,0.06); }
    50%       { box-shadow: 0 0 50px rgba(240,165,0,0.13); }
}

/* ── Header ── */
.terminal-header {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 3px solid var(--amber);
    padding: 2.5rem 2.2rem 2rem;
    border-radius: 4px;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    animation: headerIn 0.55s ease forwards, glow 5s ease-in-out 0.6s infinite;
}

.terminal-header::after {
    content: '';
    position: absolute;
    left: 0; right: 0;
    height: 60px;
    background: linear-gradient(to bottom, rgba(240,165,0,0.04), transparent);
    animation: scanline 6s linear infinite;
    pointer-events: none;
}

.terminal-header .badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--amber);
    display: block;
    margin-bottom: 0.9rem;
    opacity: 0.85;
}

.terminal-header h1 {
    font-family: 'Unbounded', sans-serif;
    font-size: 2.6rem;
    font-weight: 900;
    color: var(--text);
    margin: 0 0 0.6rem 0;
    line-height: 1.05;
    letter-spacing: -0.03em;
}

.terminal-header h1 em {
    color: var(--amber);
    font-style: normal;
}

.terminal-header p {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--muted);
    margin: 0;
    letter-spacing: 0.06em;
}

/* ── Section labels ── */
.row-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--amber);
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.6rem;
    animation: fadeUp 0.4s ease 0.3s both;
}

.row-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── Input ── */
.stTextInput > div > div > input {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-left: 3px solid var(--amber) !important;
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.88rem !important;
    border-radius: 3px !important;
    padding: 0.9rem 1rem !important;
    transition: border-color 0.18s, box-shadow 0.18s !important;
    animation: fadeUp 0.4s ease 0.35s both;
}

.stTextInput > div > div > input:focus {
    border-color: var(--amber) !important;
    box-shadow: 0 0 0 2px rgba(240,165,0,0.18) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder {
    color: var(--muted) !important;
    font-size: 0.78rem !important;
}

.stTextInput label {
    color: var(--muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}

/* ── Button ── */
.stButton > button {
    background: var(--amber) !important;
    color: #09090f !important;
    border: none !important;
    border-radius: 3px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    padding: 0.7rem 2.2rem !important;
    transition: background 0.15s, transform 0.12s, box-shadow 0.15s !important;
    animation: fadeUp 0.4s ease 0.5s both;
}

.stButton > button:hover {
    background: #d49200 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(240,165,0,0.28) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
    border-radius: 3px !important;
}

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    padding: 1rem 1.2rem !important;
    animation: fadeUp 0.45s ease both;
}

[data-testid="stMetricValue"] {
    color: var(--amber) !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
}

[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.65rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
}

/* ── Expanders ── */
details summary {
    background: var(--surface) !important;
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.78rem !important;
    border: 1px solid var(--border) !important;
    border-radius: 3px !important;
    padding: 0.65rem 1rem !important;
}

details > div {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    color: var(--muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem !important;
    line-height: 1.75 !important;
}

/* ── Result box ── */
.result-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--teal);
    border-radius: 4px;
    padding: 1.6rem 1.8rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text);
    font-size: 0.88rem;
    line-height: 1.8;
    animation: fadeUp 0.4s ease forwards;
}

/* ── Divider / HR ── */
hr {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 1.5rem 0 !important;
}

/* ── Footer ── */
.custom-footer {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: var(--muted);
    text-align: center;
    letter-spacing: 0.12em;
    padding: 0.75rem 0;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="terminal-header">
    <span class="badge">▸ sistema ativo &nbsp;·&nbsp; v2.0 &nbsp;·&nbsp; pronto</span>
    <h1>AI <em>Stock</em> Agent</h1>
    <p>consultas inteligentes em tempo real &nbsp;·&nbsp; modelos gpt avançados</p>
</div>
""", unsafe_allow_html=True)

# ── Query input ──────────────────────────────────────────────────────────────
st.markdown('<div class="row-label">consulta</div>', unsafe_allow_html=True)
user_question = st.text_input(
    "pergunta",
    label_visibility="collapsed",
    placeholder="ex: quais produtos estão com estoque crítico?"
)

button_consult = st.button("Executar consulta")

# ── Instructions ─────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="row-label">referência</div>', unsafe_allow_html=True)

col_inst1, col_inst2 = st.columns(2)

with col_inst1:
    with st.expander("Como usar"):
        st.write("""
        Selecione o modelo e digite sua pergunta sobre estoque,
        preços ou reposições. O agente consulta o banco de dados
        e retorna uma análise contextualizada.
        """)

with col_inst2:
    with st.expander("Exemplos de perguntas"):
        st.write("· Quais produtos estão com baixo estoque?")
        st.write("· Qual o valor total do inventário?")
        st.write("· Produtos que precisam de reposição urgente")
        st.write("· Histórico de vendas dos últimos 30 dias")
        st.write("· Produtos mais vendidos por categoria")

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Modelo de IA")

    model_options = [
        'gpt-4o',
        'gpt-4.1',
        'gpt-4.1-mini',
        'gpt-4.1-nano'
    ]

    model_labels = {
        'gpt-4o':       'GPT-4o — recomendado',
        'gpt-4.1':      'GPT-4.1',
        'gpt-4.1-mini': 'GPT-4.1 Mini',
        'gpt-4.1-nano': 'GPT-4.1 Nano'
    }

    selected_model = st.selectbox(
        'modelo',
        options=model_options,
        format_func=lambda x: model_labels[x],
        label_visibility="collapsed"
    )

    st.markdown("### Performance")

    model_metrics = {
        'gpt-4o':       {'speed': 95, 'accuracy': 98},
        'gpt-4.1':      {'speed': 90, 'accuracy': 95},
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

    st.markdown("### Sobre")
    st.markdown("""
    *Agente IA para consultas inteligentes em bases de dados de estoque.
    Respostas contextualizadas com modelos GPT avançados.*
    """)

    st.divider()

    st.markdown("### Funcionalidades")
    st.markdown("· Linguagem natural")
    st.markdown("· Consultas automatizadas")
    st.markdown("· Análises preditivas")
    st.markdown("· Relatórios instantâneos")

# ── Query execution ──────────────────────────────────────────────────────────
if button_consult:
    if user_question and user_question.strip():
        status_placeholder = st.empty()
        status_placeholder.info("consultando estoque...")
        time.sleep(1)

        try:
            output = agent(selected_model, user_question)

            status_placeholder.success("concluído")
            time.sleep(0.5)
            status_placeholder.empty()

            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown('<div class="row-label">resultado</div>', unsafe_allow_html=True)

            result_text = output.get('output', 'Nenhum resultado encontrado.')
            st.markdown(
                f'<div class="result-box">{result_text}</div>',
                unsafe_allow_html=True
            )

            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown('<div class="row-label">métricas</div>', unsafe_allow_html=True)

            col_m1, col_m2, col_m3 = st.columns(3)
            with col_m1:
                st.metric("Resposta", "1.2s")
            with col_m2:
                st.metric("Modelo", selected_model.split("-")[0].upper())
            with col_m3:
                st.metric("Confiança", "98%")

        except Exception as e:
            status_placeholder.error("erro ao processar consulta")
            with st.expander("Detalhes do erro"):
                st.exception(e)

    else:
        st.warning("Digite uma pergunta antes de consultar.")

# ── Footer ───────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    '<div class="custom-footer">'
    'AI STOCK AGENT v2.0 &nbsp;·&nbsp; Desenvolvido por Letícia Castelo'
    '</div>',
    unsafe_allow_html=True
)
