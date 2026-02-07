from flask import Blueprint, render_template, redirect, url_for, flash,abort
from flask_login import login_required
from app.forms.permission_forms import PermissionCreateForm, PermissionEditForm, PermissionConfirmDeleteForm
from app.services.permission_service import PermissionService
permission_bp = Blueprint("permissions", __name__, url_prefix="/permissions")

@permission_bp.route("/")
@login_required
def index():
    permissions = PermissionService.get_all()
    return render_template("permissions/index.html", permissions=permissions)

@permission_bp.route("/<int:permission_id>")
@login_required
def detail(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)
    return render_template("permissions/detail.html", permission=permission)

@permission_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PermissionCreateForm()
    if form.validate_on_submit():
        data = {
            "code": form.code.data,
            "name": form.name.data,
            "module": form.module.data,
            "description": form.description.data,
        }

        permission = PermissionService.create(data)
        flash(f"Permission '{permission.name}' was created successfully.", 'success')
        return redirect(url_for('permissions.index'))

    return render_template("permissions/create.html", form=form)

@permission_bp.route("/<int:permission_id>/edit", methods=["GET", "POST"])
@login_required
def edit(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    form = PermissionEditForm(original_permission=permission, obj=permission)
    if form.validate_on_submit():
        data = {
            "code": form.code.data,
            "name": form.name.data,
            "module": form.module.data,
            "description": form.description.data,
        }

        PermissionService.update(permission, data)
        flash(f"Permission '{permission.name}' was updated successfully", "success")
        return redirect(url_for("permissions.detail", permission_id=permission.id))

    return render_template("permissions/edit.html", form=form, permission_id=permission.id)

@permission_bp.route("/<int:permission_id>/delete", methods=["GET"])
@login_required
def delete_confirm(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    form =PermissionConfirmDeleteForm()
    return render_template("permissions/delete_confirm.html", permission=permission, form=form)

@permission_bp.route("/<int:permission_id>/delete", methods=["POST"])
@login_required
def delete(permission_id: int):
    permission = PermissionService.get_by_id(permission_id)
    if permission is None:
        abort(404)

    PermissionService.delete(permission)
    flash("Permission was deleted successfully.", "success")
    return redirect(url_for('permissions.index'))