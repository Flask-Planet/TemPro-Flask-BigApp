from flask import Flask

from app.extensions import bigapp
from app.extensions import db


# to run the app do this command:
# (venv)...$ flask run
# or
# (venv)...$ gunicorn
# or
# ...$ venv/bin/gunicorn

def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static"
    )
    bigapp.init_app(app)

    bigapp.import_models(from_folder="models")
    db.init_app(app)

    bigapp.import_builtins()
    # builtins must use a loader function,
    # navigate to app/builtins/requests.py
    # to see how it works

    bigapp.import_blueprints("blueprints")

    with app.app_context():
        db.create_all()

    return app
