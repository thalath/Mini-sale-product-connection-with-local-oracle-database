from extensions import db
from sqlalchemy import Identity

class Client(db.Model):
    __tablename__ ="clients"
    
    client_no = db.Column(db.Integer, Identity(start=1), primary_key=True)
    client_name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(150))
    city = db.Column(db.String(50))
    phone = db.Column(db.String(15), unique=True, nullable=False)
    client_type = db.Column(db.Integer,db.ForeignKey("client_type.client_type"), nullable=False)
    discount = db.Column(db.Float)