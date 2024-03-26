import os
from openai import OpenAI
import openai
import dotenv
from pathlib import Path
import tiktoken
import time

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

dotenv.load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPEN_API_KEY"),
    organization = os.getenv("OPEN_AI_ORGANIZATION")
)

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""
prompt_usuario = carrega("dados/lista_de_compras_10_clientes.csv")

listar_tokens = codificador.encode(prompt_usuario + prompt_sistema)
total_tokens = len(listar_tokens)

modelChoice = "gpt-3.5-turbo"
waitForExit = 2048
if total_tokens > 4096 - waitForExit:
    modelChoice = "gpt-3.5-turbo-16k"

print(f'Model choice {modelChoice}')

tentativas = 0

while tentativas < 3: 
    tentativas +=1
    #raise openai.Error.APIError
    try:
        #raise OpenAI.Error.APIError
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
        print(resposta.choices[0].message.content)
        break
    except OpenAI.error.AuthenticationError as e:
        print("Autenticação: {}".format(e))
    except OpenAI.error.APIError as e:
        print("Error de la API: {}".format(e))
    except Exception as e:
        print("Error inesperado: {}".format(e))
 
    
        


