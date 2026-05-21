# ChargeGrid Conversation AI — Sprint 1 (GoodWe Challenge 2026)

## Integrantes
* *Aline Medri Marcolino* - RM: 569349
* *Luis Fernando de Azevedo* - RM: 574167
* *Eduardo Novaki Santos Coelho* - RM:572649
*  *Gabriel dos Santos Siqueira* - RM:572200
*  *Pedro Arthir Campos Reis* - RM:569913

---

##  1. O Problema Abordado
No cenário atual de eletromobilidade, os hubs de carregamento comercial enfrentam um grande desafio técnico e operacional: a ausência de mecanismos integrados e amigáveis para orquestrar potência, registrar ciclos de carga, faturar e comunicar dados complexos aos usuários (escopo *ChargeGrid Intelligence*). 
O mercado de energia envolve conceitos técnicos densos (como kW, kWh, Tarifa Branca e eficiência de ciclo) que geram atrito e afastam o engajamento do motorista comum. Além disso, a implementação de carregamento bidirecional (V2G) esbarra no medo dos usuários quanto à degradação acelerada da bateria e nas rígidas barreiras regulatórias da ANEEL no Brasil, que dificultam transações financeiras diretas (dinheiro em conta) para o consumidor de varejo.

---

## 2. Proposta do Chatbot e Justificativa de Escopo
* *Escopo Escolhido:* ChargeGrid Intelligence (Hub de Carregamento Comercial em shoppings e eletropostos).
* *Persona Alvo:* O Motorista de Veículo Elétrico (EV) que utiliza o hub comercial.

### A Solução:
O *ChargeGrid Conversation AI* é um agente conversacional inteligente integrado ao ecossistema de carregadores e inversores GoodWe. O maior diferencial do projeto é a capacidade de *"transformar a complexidade energética em uma experiência conversacional simples, fluida e gamificada"*. 
O chatbot atua como o agregador/orquestrador (Virtual Power Plant - VPP), interagindo com o motorista para gerenciar tanto o carregamento inteligente unidirecional (V1G) quanto o bidirecional (V2G). Ele automatiza a proposta de cessão de energia nos horários de pico do estabelecimento, contorna a barreira da ANEEL ao oferecer recompensas comerciais locais (vouchers, isenção de estacionamento) e mitiga o desgaste do hardware através de um módulo proprietário de IA focado na saúde da bateria.

---

##  3. Arquitetura Tecnológica e Justificativa Técnica
Para garantir que o chatbot opere como uma ferramenta real e escalável, a stack tecnológica foi selecionada com base nos seguintes critérios:
* *Framework de Orquestração (LangChain / LlamaIndex):* Utilizado para a criação de agentes baseados em IA. Ele permite conectar o modelo de linguagem (LLM) a APIs externas de telemetria do veículo, dados do carregador e APIs de mercado energético, além de gerenciar a memória da conversação de forma dinâmica.
* *Modelo de Linguagem (OpenAI API GPT-4o-mini / Llama 3 via Groq):* Escolhido pela alta velocidade de inferência, custo-benefício e excelente capacidade de extração de intenções do usuário (como tempo de permanência e SoC desejado) e suporte nativo a Function Calling para rodar scripts de validação econômica em segundo plano.
* *Banco de Dados Vetorial (ChromaDB / Pinecone):* Utilizado para implementar a arquitetura RAG (Retrieval-Augmented Generation). Ele armazenará os manuais técnicos dos inversores GoodWe, documentações dos protocolos de comunicação e regras de negócio, garantindo respostas precisas e sem alucinações.

---

## 4. Fluxograma de Funcionamento Lógico
O sistema opera integrado em três camadas distintas, cujo fluxo lógico de dados segue a estrutura abaixo:
Entrada do usuário, processamento inteligente e geração de resposta contextualizada.


### Fluxograma

Usuário  
↓  
Interface do Chatbot  
↓  
Recebimento da Pergunta  
↓  
Injeção do Contexto GoodWe  
↓  
LangChain  
↓  
Modelo LLM (Llama 3.2 / Ollama Web)  
↓  
Processamento Inteligente  
↓  
Geração da Resposta  
↓  
Usuário
