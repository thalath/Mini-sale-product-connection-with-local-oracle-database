from extensions import db
from sqlalchemy import Identity

class Product_type(db.Model):
    __tablename__ = "product_types"
    producttype_id = db.Column(db.Integer, Identity(start=1), primary_key=True)
    producttype_name = db.Column(db.String(50), unique=True, nullable=False)
    remark = db.Column(db.String(20))
    
    
