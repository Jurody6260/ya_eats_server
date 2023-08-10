from flask import Flask, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .utils.register_bp import register_blueprints
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_pyfile('configs/prod.py')
    from app.models.main import Product, Category
    babel = Babel()
    babel.init_app(app)
    db.init_app(app)
    app = register_blueprints(app)

    with app.app_context():
        db.create_all()
        if Product.query.count() == 0:
            from .utils.consts import prdcts
            print(prdcts)
            cat_id = Category(name='Main').save()['id']
            for i in prdcts:
                i.category_id = cat_id
                i.save()
    admin = Admin(app, name='Ya_Eats', template_mode='bootstrap4')
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Category, db.session))
    return app
