from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(
    api_key= os.getenv("OPEN_API_KEY"),
    organization = os.getenv("org-mspWTj37jtqb6ANO1lXSbeL4")
)

response = chat_completion = client.chat.completions.create(
    messages=[
             {
       "role" : "system",
         "content" : "Você é um assistente apenas sobre reserva de veículo. "
      },
      {
       "role" : "user",
         "content" : "tenta extrai as seguintes informações: Data de retirada, Data de devolução, Local da retirada, E se tem algum tipo de veículo"
         }
    ],
    model="gpt-3.5-turbo",
)

print(response)
