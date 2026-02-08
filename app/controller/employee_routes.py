from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required
from app.services.employee_service import EmployeeService
from app.forms.employee_forms import EmployeeCreateForm, EmployeeEditForm, EmployeeConfirmDeleteForm
employee_bp = Blueprint("employees", __name__, url_prefix="/employees")

@employee_bp.route("/")
@login_required
def index():
    employees = EmployeeService.get_all()
    return render_template("employees/index.html", employees=employees)


@employee_bp.route("/<int:employee_id>")
@login_required
def detail(employee_id: int):
    employee = EmployeeService.get_by_id(employee_id)
    if employee is None:
        abort(404)
    return render_template("employees/detail.html", employee=employee)

@employee_bp.route("/create", methods=["GET", "POST"])
def create():
    form = EmployeeCreateForm()
    if form.validate_on_submit():
        data= {
            "employeename": form.employeeName.data,
            "gender": form.gender.data,
            "birthdate": form.birthdate.data,
            "JOB_ID": form.JOB_ID.data,
            "ADDRESS": form.ADDRESS.data,
            "PHONE": form.PHONE.data,
            "SALARY": form.SALARY.data or 0.00,
            "REMARK": form.REMARK.data or "Normal"
        }
        photo = form.PHOTO.data
        
        JOB_ID = form.JOB_ID.data or None

        emp = EmployeeService.create(data, photo, JOB_ID)
        flash(f"Employee: '{emp.employeename}' was added successfully!", "success")
        return redirect(url_for("employees.index"))
    
    return render_template("employees/create.html", form=form)

@employee_bp.route("/<int:employee_id>/edit", methods=["GET", "POST"])
def edit(employee_id: int):
    emp = EmployeeService.get_by_id(employee_id)

    if emp is None:
        abort(404)
        
    form = EmployeeEditForm(original_emp=emp)
    if form.validate_on_submit():
        data= {
            "employeename": form.employeeName.data,
            "gender": form.gender.data,
            "birthdate": form.birthdate.data,
            "JOB_ID": form.JOB_ID.data,
            "ADDRESS": form.ADDRESS.data,
            "PHONE": form.PHONE.data,
            "SALARY": form.SALARY.data or 0.00,
            "REMARK": form.REMARK.data or "Normal"
        }
        
        photo = form.PHOTO.data or "image/jpeg"
        
        EmployeeService.update(emp, data, photo)
        flash(f"Employee '{emp.employeename}' updated successfully", "success")
        return redirect(url_for("employees.index"))
    
    return render_template("employees/edit.html", form=form, emp=emp.employeeid)

@employee_bp.route("/<int:employee_id>/delete", methods=["GET"]) #methods get: just called data from database and asked for delete
@login_required
def delete_confirm(employee_id: int):
    emp = EmployeeService.get_by_id(employee_id)
    if emp is None:
        abort(404)

    form = EmployeeConfirmDeleteForm()
    return render_template("employees/delete_confirm.html", emp=emp, form=form)


@employee_bp.route("/<int:employee_id>/delete", methods=["POST"]) # methods post: confirm deleted data from database 
@login_required
def delete(employee_id: int):
    emp = EmployeeService.get_by_id(employee_id)
    if emp is None:
        abort(404)

    EmployeeService.delete(emp)
    flash("User was deleted successfully.", "success")
    return redirect(url_for("employees.index"))