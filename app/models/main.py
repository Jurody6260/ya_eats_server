from app.utils.base import db, BaseModel

class Product(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    
class Category(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    products = db.relationship("Product", backref="category")