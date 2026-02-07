from extensions import db
from datetime import datetime
from app.models.association import user_roles, role_permissions
from sqlalchemy import Identity

class Role(db.Model):
    __tablename__ = "ROLES"
    id = db.Column(db.Integer, Identity(start=1), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    users = db.relationship("User", secondary=user_roles, back_populates="roles")
    permissions = db.relationship("Permission", secondary=role_permissions, back_populates="roles")

    def has_permission(self, permission_code: str) -> bool:
        return any(p.code == permission_code for p in self.permissions)

    def __repr__(self) -> str:
        return f"<Role {self.name}'>"



