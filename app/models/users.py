from extensions import db
from datetime import datetime
from flask_login import UserMixin
from app.models.association import user_roles
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Identity

class User(UserMixin, db.Model):
    __tablename__ = "USERS"
    id = db.Column(db.Integer, Identity(start=1), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(225), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    password_hash = db.Column(db.String(225), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    roles = db.relationship("Role", secondary=user_roles, back_populates="users")
    
    
    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def has_role(self, role_name: str) -> bool:
        return any(role.name == role_name for role in self.roles)

    def get_permission_codes(self) -> set[str]:
        return {perm.code for role in self.roles for perm in role.permissions}
    
    def has_permission(self, permission_code: str) -> bool:
        return permission_code in self.get_permission_codes()

    def __repr__(self):
        return f"<User {self.username}>"

