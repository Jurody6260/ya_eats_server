from flask import jsonify, redirect, Blueprint

from app.models.main import Category, Product, db

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/")
def hello():
    return jsonify({"title": "hello world from flask"})

@api.get('/fix')
def fix():
    for i in Product.query.all():
        i.image = "static/" + i.image
    # db.session.commit()
    return 'ok'

@api.get('/products')
def products():
    return jsonify([i.to_json() for i in Product.query.all()])


@api.get('/categories')
def categories():
    return jsonify([i.to_json() for i in Category.query.all()])