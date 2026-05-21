from llm_client import LLMClient
from prompt_builder import montar_prompt

def executar_chatbot(pergunta):

    with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
        contexto = f.read()

    prompt = montar_prompt(contexto, pergunta)

    client = LLMClient()

    resposta = client.generate(prompt)

    return resposta