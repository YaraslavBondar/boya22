from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from core.db import db
    db.init_app(app)


    with app.app_context():
        from core import views
        from dynamic_inputs import dynamic_inputs

        app.register_blueprint(dynamic_inputs)

    return app
