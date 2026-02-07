from extensions import db

user_roles = db.Table(
    "user_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("USERS.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("ROLES.id"), primary_key=True)
)

role_permissions = db.Table(
    "ROLE_PERMISSIONS",
    db.Column("role_id", db.Integer, db.ForeignKey("ROLES.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("PERMISSIONS.id"), primary_key=True)
)