from openai import OpenAI
import os
import dotenv


dotenv.load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPEN_API_KEY"),
    organization = os.getenv("OPEN_AI_ORGANIZATION")
)


audio_file = open("criando-postagem-instagram/transcricaoaudio/mpthreetest.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
with open(f"criando-postagem-instagram/transcricaoaudio/texto_completo.txt", "w",encoding='utf-8') as arquivo_texto:
    arquivo_texto.write(transcript.text)
print(transcript.text)
