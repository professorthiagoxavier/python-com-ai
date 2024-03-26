# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPEN_API_KEY"),
    organization = os.getenv("OPEN_AI_ORGANIZATION")
)

def categorizaVeiculo(veiculo, categorias):
    prompt_sistema = f"""
    Você é um categorizador de veículos. 
    Se e a entrada veiculo não corresponder a um veículo, responda "Por aqui falamos apenas de veículos".
    Você pode utilizar a lista abaixo para categorizar: 
    Se as categorias abaixo não forem sobre veículos, responda com "Desculpe, mas não consigo ajudar"
    #### Lista de categorias válidas
    {categorias}
    """
    response = client.chat.completions.create(
        messages =[
            {
                "role" : "system", 
                "content":prompt_sistema
            }, 
            {
                "role" : "user", 
                "content": veiculo
            }
        ],
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0, 
        n = 3 #inserir retornos. 
    )
    print(response.choices[0].message.content)

print("Categorias válidas: ")   
categorias = input()
output = True
while output: 
    print("Digite o nome do veículo: ")
    nome_do_veiculo = input()
    categorizaVeiculo(nome_do_veiculo, categorias)
    
    print("Deseja continuar? [s|n]")
    confirmOutput = input()
    output = True if confirmOutput == "s" else False
    if confirmOutput == "n":
        break
    
    




