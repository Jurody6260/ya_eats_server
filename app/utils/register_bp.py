from flask import Flask


def register_blueprints(app: Flask):
    from ..blueprints.api import api as api_bp
    app.register_blueprint(api_bp)
    
    return app