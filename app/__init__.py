from flask import Flask
from strawberry.flask.views import GraphQLView

from app.graphql.schema import schema
from app.config import get_db, test_connection


def create_app():
    app = Flask(__name__)

    test_connection()

    app.add_url_rule(
        rule="/graphql",
        view_func=GraphQLView.as_view(
            name="graphql_view",
            schema=schema
        )
    )

    return app