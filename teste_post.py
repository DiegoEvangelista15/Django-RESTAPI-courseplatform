import requests

headers = {'Authorization': 'Token b095e3ee3594b80b1afca1dc0aa0328ff5cb973a'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    'titulo':'Tudo sobre Scrum',
    'url': 'https://www.treasy.com.br/blog/scrum/'  
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HTTP 201
print(resultado.status_code)
assert resultado.status_code == 201

# testando se o titulo do curso retornado e o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']