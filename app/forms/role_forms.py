from collections import defaultdict
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Role, Permission
from extensions import db
from app.forms.multi_checkbox_field import MultiCheckBoxField

def _permission_choices():
    """Flate (idm label) list, userd for filed binding only"""
    return [
        (perm.id, f"{perm.code} - {perm.name}")
        for perm in db.session.scalars(
            db.select(Permission).order_by(Permission.code)
        )
    ]
    
def _permissions_grouped_by_module():
    """
    Return permissions grouped by module
    {
        "User": [Permission, ...],
        "Roles": [Permission, ...],
        ...
    }
    """
    
    perms = list(
        db.session.scalars(
            db.select(Permission).order_by(
                Permission.module, Permission.code
            )
        )
    )
    
    grouped = defaultdict(list)
    for perm in perms:
        module = perm.module or "General"
        grouped[module].append(perm)
    return dict(grouped)

class RoleCreateForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=80)],
        render_kw={"placeholder": "Role Name"}
    )
    
    description = TextAreaField(
        "Description",
        render_kw={"placeholder": "Short description (optional)"},
    )
    
    permission_ids = MultiCheckBoxField(
        "Permissions",
        coerce=int,
        render_kw={"placeholder": "Permissions granted to this role"},
    )
    
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_ids.choices = _permission_choices()
        self.permissions_by_module = _permissions_grouped_by_module()

    def validate_name(self, field):
        exists = db.session.scalar(
            db.select(Role).filter(Role.name == field.data)
        )
        if exists:
            raise ValidationError("this role name is already token.")


class RoleEditForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=80)],
    )
    
    description = TextAreaField(
        "Description",
        render_kw={"placeholder": "Short description (optional)"},
    )
    
    permission_ids = MultiCheckBoxField(
        "Permissions",
        coerce=int,
        render_kw={"placeholder": "Permissions granted to this role"},
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_role: Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_role = original_role
        self.permission_ids.choices = _permission_choices()
        self.permissions_by_module = _permissions_grouped_by_module()
        
        if not self.is_submitted():
            self.permission_ids.data = [p.id for p in original_role.permissions]
        
        
    


class RoleConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")