import requests

# GET para Avaliacoes

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
print(avaliacoes.status_code)  # para verificar o codigo de resposta dele

# Acessando dados

print(avaliacoes.json())
print(type(avaliacoes.json()))  # na verdade ele gera um dict python

#acessando quantidade de dados
print(avaliacoes.json()['count'])

#acessando a proxima pag de resultos
print(avaliacoes.json()['next']) 

#acessando os resultados desta pagina
print(avaliacoes.json()['results'])

# acessando o primeiro elemento da lista de resulta
print(avaliacoes.json()['results'][0])

# acessando o ultimo elemento da lista de resulta
print(avaliacoes.json()['results'][-1])

# acessando o nome do resultado
print(avaliacoes.json()['results'][0]['nome'])

#GET de uma avaliacao especifica

avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/5')
print(avaliacao.json())

#  GET para cursos = com bloqueio

cursos = requests.get('http://127.0.0.1:8000/api/v2/cursos')
print(cursos.status_code)
print(cursos.json())

# precisa ter o header
header = {"Authorization": 'Token b095e3ee3594b80b1afca1dc0aa0328ff5cb973a'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos', headers=header)
print(cursos.status_code)
print(cursos.json())