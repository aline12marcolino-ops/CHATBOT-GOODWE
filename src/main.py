from chatbot import executar_chatbot

print("=== CHATBOT GOODWE ===")

while True:

    pergunta = input("\nDigite sua pergunta: ")

    if pergunta.lower() == "sair":
        break

    resposta = executar_chatbot(pergunta)

    print("\nResposta:")
    print(resposta)