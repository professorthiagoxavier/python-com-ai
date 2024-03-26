import openai
from dotenv import load_dotenv
import os


client = any

def openai_whisper_transcrever(caminho, nome_arquivo, client, key):
    
    print(f'transcricao whisper {caminho}')
    
    audio = open(caminho, "rb")
    resposta = openai.Transcription.create(
        model = "whisper-1",
        api_key = key,
        file = audio
    )
    transcricao = resposta.text
    
    # with open(f"texto_completo_{nome_arquivo}.txt", "w",encoding='utf-8') as arquivo_texto:
    #     arquivo_texto.write(transcricao)
        
    # return transcricao

def main(): 
    load_dotenv()

    caminho=  "criando-postagem-instagram/transcricaoaudio/mpthreetest.mp3"
    nome_arquivo = "mpthreetest"
    url_podcast = ""
    modelo = "whisper-1"
    transcricao_completa = openai_whisper_transcrever(caminho, nome_arquivo, client, os.getenv("OPEN_API_KEY"))
     
if __name__ == "__main__":
    main()
    
    
    