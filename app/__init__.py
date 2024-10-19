from flask import Flask
from strawberry.flask.views import GraphQLView

from app.graphql.schema import schema
from config import get_db

def create_app():
    app = Flask(__name__)

    app.config['db'] = get_db()

    app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql_view", schema=schema))

    return app