import os
from openai import OpenAI
import dotenv
from pathlib import Path
import tiktoken

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo")

def carrega(nome_do_arquivo):
    try:
        directory_path = Path(__file__).resolve().parent
        csv_file_path = directory_path / nome_do_arquivo
        with csv_file_path.open(mode='r') as file:
            dados = file.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")
        
def salva(nome_arquivo, conteudo):
    try: 
        directory_path = Path(__file__).resolve().parent
        file = directory_path / nome_arquivo
        with file.open(mode='w', encoding="utf-8") as file:
            for linha in conteudo:
                file.write(linha.message.content)
                file.write("\n***********\n")
                
    except IOError as e: 
        print(f"Erro: {e}")      

             

dotenv.load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPEN_API_KEY"),
    organization = os.getenv("OPEN_AI_ORGANIZATION")
)

prompt_sistema = """
Você é um analista de sentimentos de avaliações de produto. Como um NPS.
Escreva um resumo de no máximo 20 palavras e, resuma as avaliações incluindo o sentimento. 
#### Formato da saida
Nome do produto: 
Resumo das avaliações: [pode utilizar as anotações do NPS: POSITIVO, NEUTRO, NEGATIVO]
Pontos fortes: [3 bullets points]
Pontos fracos: [3 bullets points]
"""
prompt_usuario = carrega("dados/avaliacoes-Tapete de yoga.txt")

listar_tokens = codificador.encode(prompt_usuario + prompt_sistema)
total_tokens = len(listar_tokens)

modelChoice = "gpt-3.5-turbo"
waitForExit = 2048
if total_tokens > 4096 - waitForExit:
    modelChoice = "gpt-3.5-turbo-16k"

print(f'Model choice {modelChoice}')

resposta = client.chat.completions.create(
        messages =[
            {
                "role" : "system", 
                "content":prompt_sistema
            }, 
            {
                "role" : "user", 
                "content": prompt_usuario
            }
        ],
        model=modelChoice,
        temperature=1,
        max_tokens=waitForExit, #limiting total tokens 
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0, 
        n = 3 #inserir retornos. 
)

salva("dados/tapete-avaliacao.txt",  resposta.choices)
