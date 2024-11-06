from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger
from .api import ApiResource


def create_app():
    app = Flask(__name__, template_folder='../html')

    '''
    auth = HTTPBasicAuth()
    USER_DATA = {
        "admin": "admin123"
    }

    @auth.verify_password
    def verify(username, password):
        if not (username and password):
            return False
        return USER_DATA.get(username) == password
    
    class PrivateResource(Resource):
        @auth.login_required
        def get(self):
            return {"Ok!": 42}
    '''
     
    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'API VitiBrasil',
        'uiversion': 3
    }
    Swagger(app)

    api = Api(app)
    # Adicionando o recurso para api
    api.add_resource(ApiResource, '/api/')

    # Rota para Página Inicial
    @app.route('/')
    def welcome():
        return render_template('index.html')

    return app