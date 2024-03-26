import tiktoken

codificado = tiktoken.encoding_for_model("gpt-3.5-turbo")
lista_de_tokens = codificado.encode("Teste de quantidade de tokens")
print(lista_de_tokens)
print(len(lista_de_tokens))
