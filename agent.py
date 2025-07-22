import os
from decouple import config 

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

def agent(select_model, user_question):

    model = ChatOpenAI(
        model = select_model
    )

    db = SQLDatabase.from_uri('sqlite:///estoque.db')

    toolkit = SQLDatabaseToolkit(
        db=db,
        llm=model
    )

    system_message = hub.pull('hwchase17/react') 

    agent = create_react_agent(
        llm=model,
        tools=toolkit.get_tools(),
        prompt=system_message
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=toolkit.get_tools(),
        verbose=True,
        handle_parsing_errors=True
    )

    prompt = ''''
    Use as ferramentas necessárias para responder as perguntas relacionadas ao estoque de produtos. 
    Você fornecerá insights sobre produtos, preços, reposições de estoque e relatórios conforme 
    for solicitado pelo usuário. A resposta final deve ter uma formatação amigável de visualização para o usuário.
    Sempre responda em português brasileiro.
    Pergunta: {q}
    '''

    prompt_template = PromptTemplate.from_template(prompt)
    formatted_prompt = prompt_template.format(q=user_question)
    output = agent_executor.invoke({'input': formatted_prompt})
    return output