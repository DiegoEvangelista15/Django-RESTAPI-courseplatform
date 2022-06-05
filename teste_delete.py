import requests

headers = {'Authorization': 'Token b095e3ee3594b80b1afca1dc0aa0328ff5cb973a'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}8/', headers=headers)

# Testando o codigo de status HTTP 204
print(resultado.status_code)
assert resultado.status_code == 204

