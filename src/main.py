# Importa diretamente a classe que criamos no llm_client
from llm_client import LLMClient

print("=== CHATBOT GOODWE ===")

# Instancia o cliente ANTES do loop para preservar o histórico na memória do objeto
bot = LLMClient()

while True:
    pergunta = input("\nDigite sua pergunta: ")
    
    if pergunta.lower() == "sair":
        print("Encerrando o chat. Até logo!")
        break
        
    if not pergunta.strip():
        continue
        
    # O método .generate() agora trata internamente de guardar o histórico e responder
    resposta = bot.generate(pergunta)
    
    print("\nResposta:")
    print(resposta)
    print("-" * 50)