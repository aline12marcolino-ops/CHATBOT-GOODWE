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

    def generate(self, prompt):

        resposta = self.client.chat(
            model="gpt-oss:120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return resposta["message"]["content"]