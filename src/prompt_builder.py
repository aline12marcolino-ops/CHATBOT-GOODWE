def montar_prompt(contexto, pergunta):
    prompt = f"""
CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

RESPONDA DE FORMA OBJETIVA.
"""

    return prompt