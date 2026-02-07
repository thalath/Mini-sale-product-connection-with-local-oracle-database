from extensions import db
from datetime import datetime
from sqlalchemy import Identity

class Invoice(db.Model):
    __tablename__ = "invoices"
    invoiceno = db.Column(db.Integer, Identity(start=1), primary_key=True)
    invoice_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    cline_no = db.Column(db.Integer, db.ForeignKey("clients.client_no"), nullable=False)
    employeeid = db.Column(db.Integer, db.ForeignKey("employees.employeeid"), nullable=False)
    invoice_status = db.Column(db.String(100))
