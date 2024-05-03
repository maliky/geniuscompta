import os
from flask import Flask, Blueprint
from . import main

def create_app(test_config=None):
    # création de l'application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # à changer par une nonce
        DATABASE=os.path.join(app.instance_path, "flask.sqlite"),
    )

    if test_config is None:
        # charger une instance du fichier de config s'il existe
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.register_blueprint(main.bp)
    
    return app

