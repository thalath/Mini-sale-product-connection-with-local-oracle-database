from extensions import db
from sqlalchemy import Identity

class Client(db.Model):
    __tablename__ = "client_type"

    client_type = db.Column(db.Integer, nullable=False, primary_key=True)
    type_name = db.Column(db.String(20), unique=True, nullable=False)
    discount_rate = db.Column(db.Float, default=0)
    remark = db.Column(db.String(15))
    
    def __repr__(self):
        return f"Client_type '{self.type_name}'>"

