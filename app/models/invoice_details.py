from extensions import db
from sqlalchemy import ForeignKey

class Invoice_detail(db.Model):
    __tablename__ = "invoice_details"
    invoice_no = db.Column(db.Integer, db.ForeignKey("invoices.invoice_no"), primary_key=True)
    product_no = db.Column(db.String(20))
    qty = db.Column(db.Integer)
    price = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Invoice: '{self.invoice_no}'>"
