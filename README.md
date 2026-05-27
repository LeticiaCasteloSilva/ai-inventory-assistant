# AI Stock Agent

Assistente inteligente para consultas em linguagem natural sobre estoque de produtos. Utiliza **Streamlit** como interface, **LangChain** para orquestração do agente e modelos **GPT** para interpretar perguntas e consultar o banco de dados automaticamente.

## Requisitos

- Python 3.10 ou superior
- Chave de API da [OpenAI](https://platform.openai.com/api-keys)

## Instalação

```bash
git clone <url-do-repositorio>
cd ai-chatbot-streamlit

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sk-...
```

## Executando

```bash
streamlit run app.py
```

Acesse em: [http://localhost:8501](http://localhost:8501)

## Stack

- [Streamlit](https://streamlit.io) — interface web
- [LangChain](https://python.langchain.com) — orquestração do agente ReAct
- [LangChain OpenAI](https://python.langchain.com/docs/integrations/llms/openai) — integração com modelos GPT
- [SQLite](https://www.sqlite.org) — banco de dados local
- [python-decouple](https://github.com/HBNetwork/python-decouple) — variáveis de ambiente
