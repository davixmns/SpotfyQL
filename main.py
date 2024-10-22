import os

from app import create_app


if __name__ == "__main__":
    is_development = os.getenv("FLASK_ENV") == "development"
    create_app().run(host="localhost", port=5000, debug=is_development)
