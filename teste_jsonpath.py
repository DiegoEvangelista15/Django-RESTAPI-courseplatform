import json
import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')  # faz uma lista com os resultados
print(resultados)

nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)

todas_avaliacoes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(todas_avaliacoes)