import os
from openai import OpenAI
import dotenv
import json
from pathlib import Path

dotenv.load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPEN_API_KEY"),
    organization = os.getenv("OPEN_AI_ORGANIZATION")
)

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

def identifica_perfis(lista_de_compras_por_cliente):
  print("1. Iniciando identificação de perfis")
  prompt_sistema = """
  Identifique o perfil de compra para cada cliente a seguir.

  O formato de saída deve ser em JSON:

  {
    "clientes": [
      {
        "nome": "nome do cliente",
        "perfil": "descreva o perfil do cliente em 3 palavras"
      }
    ]
  } 
  """
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
                  
        
        
        
        
        