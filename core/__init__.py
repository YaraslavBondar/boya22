from flask import Flask
from core.db import db, migrate


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from core import views
        from dynamic_inputs import dynamic_inputs

        app.register_blueprint(dynamic_inputs)

    return app
