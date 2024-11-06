from waitress import serve
from misc import create_app
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth


def show_usage():
    print("""
    Bem-vindo(a) a API de consulta dos dados Vitivinicultura (Embrapa)

    Para acessar a página inicial, utilize o link abaixo:
    http://127.0.0.1:5000/
    
    Para acessar o Swagger da API, acesse:
    http://127.0.0.1:5000/apidocs/

    Para utilização da API, selecione o seguinte endpoint no seu navegador ou em uma ferramenta de execução, como o Postman:
    http://127.0.0.1:5000/api/?ano=<ano>&opcao=<opcao>&subopcao=<subopcao>

    Substitua <ano>, <opcao> e <subopcao> pelos valores desejados.

    Exemplo:
    http://127.0.0.1:5000/api/?ano=2023&opcao=opt_03&subopcao=opt_02
    """)

app = create_app()

if __name__ == "__main__":
    show_usage()
    print("Em execução...")  # Mensagem antes de iniciar o servidor
    serve(app, host='0.0.0.0', port=5000)