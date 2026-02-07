from typing import List, Optional
from app.models.permissions import Permission
from extensions import db

class PermissionService:
    @staticmethod
    def get_all() -> List[Permission]:
        return Permission.query.order_by(Permission.code.asc()).all()

    @staticmethod
    def get_by_id(permission_id: int) -> Optional[Permission]:
        return Permission.query.get(permission_id)

    @staticmethod
    def create(data: dict) -> Permission:
        perms = Permission(
            code=data["code"],
            name=data["name"],
            module=data.get("module", "General"),
            description=data.get("description") or "",
        )  
        db.session.add(perms)
        db.session.commit()
        return perms

    @staticmethod
    def update(permission: Permission, data: dict) -> Permission:
        permission.code = data["code"]
        permission.name = data["name"]
        permission.module = data.get("module", "General")
        permission.description = data.get("description") or ""
        
        db.session.commit()
        return permission

    @staticmethod
    def delete(permission: Permission) -> None:
        db.session.delete(permission)
        db.session.commit()