import requests

headers = {'Authorization': 'Token b095e3ee3594b80b1afca1dc0aa0328ff5cb973a'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultados = requests.get(url=url_base_cursos, headers=headers)

print(resultados.json())

# Testando se o endpoint esta correto
print(resultados.status_code)
assert resultados.status_code == 200  # lembrando que put tambem e 200

# pode usar o pytest com todos os modos de uma vez
