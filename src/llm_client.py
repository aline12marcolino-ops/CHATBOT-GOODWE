import os
from ollama import Client
from dotenv import load_dotenv

load_dotenv()

class LLMClient:

    def __init__(self):
        api_key = os.getenv("OLLAMA_API_KEY")
        
        self.client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": f"Bearer {api_key}"
            }
        )
        
        caminho_prompt = "system_prompt.txt" 
        if os.path.exists(caminho_prompt):
            with open(caminho_prompt, "r", encoding="utf-8") as f:
                system_prompt = f.read()
        else:
            system_prompt = "Instrução do sistema não encontrada."

        self.history = [
            {"role": "system", "content": system_prompt}
        ]

    def generate(self, prompt):
        self.history.append({"role": "user", "content": prompt})

        resposta = self.client.chat(
            model="gpt-oss:120b",
            messages=self.history
        )
        
        bot_content = resposta["message"]["content"]

        self.history.append({"role": "assistant", "content": bot_content})

        return bot_content