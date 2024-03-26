import openai

api_key = ""  
# Configura tu clave API
openai.api_key = api_key

try:
    raise Exception("x should not be greater than 5")
    raise OpenAI.Error.APIError
    response = openai.ChatCompletion.create(model="text-davinci-003", messages=[{"role": "system", "content": "Hello, how are you?"}])

    print(response)

except openai.OpenAIError as e:
    print("Error de autenticación: {}".format(e))
except openai.error.TooManyRequestsError as e:
     print("Error de autenticación: {}".format(e))
except Exception as e:
    print("Error inesperado: {}".format(e))
