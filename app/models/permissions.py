from extensions import db
from datetime import datetime
from app.models.association import role_permissions
from sqlalchemy import Identity

class Permission(db.Model):
    __tablename__="PERMISSIONS"

    id = db.Column(db.Integer, Identity(start=1), primary_key=True)
    code = db.Column(db.String(64), unique=True, nullable=False, index=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255))
    module = db.Column(db.String(80), nullable=False, default="General")
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    roles = db.relationship("Role", secondary=role_permissions, back_populates="permissions")

    def __repr__(self):
        return f"<Permission '{self.name}'>"
    
    
