from extensions import db

class Product(db.Model):
    __tablename__ = "products"
    product_no = db.Column(db.Integer, nullable=False, primary_key=True)
    productname = db.Column(db.String(40), uniqyw=True, nullable=False)
    producttype = db.Column(db.Integer, db.ForeignKey("product_types.producttype_id"), nullable=False)
    profit_percent = db.Column(db.Integer, nullable=False)
    unit_meansure = db.Column(db.String(15), nullable=False)
    reorder_level = db.Column(db.Integer, nullable=False)
    sell_price = db.Column(db.Integer, nullable=False)
    cost_price = db.Column(db.Interger, nullable=False)
    qty_on_hand = db.Column(db.Integer, default=0)
    photo = db.Column(db.BLOB)
    
    
    def __repr__(self):
        return f"<Product: '{self.productname}'>"