# app./forms.permission_forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.permissions import Permission
from extensions import db


MODULE_CHOICES = [
    ("Roles", "Roles"),
    ("Users", "Users"),
    ("Permissions", "Permissions"),
    ("System", "System"),
    ("Audit", "Audit"),
    ("General", "General"),
]


class PermissionCreateForm(FlaskForm):
    code = StringField(
        "Code",
        validators=[DataRequired(), Length(min=2, max=64)],
        render_kw={"placeholder": "e.g. users.view"}
    )
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=120)],
        render_kw={"placeholder": "Permission Name"}
    )
    
    module = SelectField(
        "Module",
        choices=MODULE_CHOICES,
        default="General",
    )
    
    description = TextAreaField(
        "Description",
        render_kw={"placeholder": "What does this permission allow"},
    )
    
    submit = SubmitField("Save")

    def validate_code(self, field):
        exists = db.session.scalar(
            db.select(Permission).filter(Permission.code == field.data)
        )
        if exists:
            raise ValidationError("this Permission name is already token.")


class PermissionEditForm(FlaskForm):
    code = StringField(
        "Code",
        validators=[DataRequired(), Length(min=2, max=64)],
        render_kw={"placeholder": "e.g. users.view"}
    )
    
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=80)],
    )
    module = SelectField(
        "Module",
        choices=MODULE_CHOICES,
        default="General"
    )
    
    description = TextAreaField(
        "Description"
    )

    submit = SubmitField("update")
    
    def __init__(self, original_permission: Permission, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_permission =  original_permission
        if not self.is_submitted():
            self.module.data = original_permission.module
        
        
    def validate_code(self, field):
        q = db.select(Permission).filter(
            Permission.code == field.data,
            Permission.id != self.original_permission.id,
        )
        exists = db.session.scalar(q)
        if exists:
            raise ValidationError("this Permission code is already in used.")
    def validate_name(self, field):
        q = db.select(Permission).filter(
            Permission.code == field.data,
            Permission.id != self.original_permission.id,
        )
        exists = db.session.scalar(q)
        if exists:
            raise ValidationError("this Permission name is already token.")


class PermissionConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")