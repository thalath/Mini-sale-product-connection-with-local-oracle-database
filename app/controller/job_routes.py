from flask import Blueprint, redirect, render_template, flash, abort, url_for
from flask_login import login_required
from extensions import db
from app.services.job_services import JobService
from app.forms.job_forms import JobCreateForm, JobEditForm, JobConfirmDeleteForm

job_bp = Blueprint("jobs", __name__, url_prefix="/jobs")

@job_bp.route("/")
@login_required
def index():
    jobs = JobService.get_all()
    return render_template("jobs/index.html", jobs=jobs)

@job_bp.route("/<int:job_id>")
def detail(job_id: int):
    job = JobService.get_by_id(job_id)
    if job is None:
        abort(404)

    return render_template("jobs/detail.html", job=job)

@job_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = JobCreateForm()

    if form.validate_on_submit():
        data = {
            "job_title": form.job_title.data,
            "min_salary": form.min_salary.data or 0.00,
            "max_salary": form.max_salary.data or 0.00
        }
        
        job = JobService.create(data)
        flash(f"Job '{job.job_title}' was created successfullty", "success")
        return redirect(url_for("jobs.index"))
    return render_template("jobs/create.html", form=form)


@job_bp.route("/<int:job_id>", methods=["GET", "POST"])
def edit(job_id: int):
    job = JobService.get_by_id(job_id)

    if job is None:
        abort(404)

    form = JobEditForm(original_job=job, obj=job)

    if form.validate_on_submit():
        data = {
            "job_title": form.job_title.data,
            "min_salary": form.min_salary.data,
            "max_salary": form.max_salary.data
        }
        
        JobService.update(job, form)
        flash(f"Job: '{job.job_title}' was updated successfully", "success")
        return redirect(url_for("jobs.detail", job_id = job.job_id))
    
    return render_template("jobs/edit.html", form=form, job=job )


@job_bp.route("/<int:job_id>/delete", methods=["GET"]) #methods get: just called data from database and asked for delete
@login_required
def delete_confirm(job_id: int):
    job = JobService.get_by_id(job_id)
    if job is None:
        abort(404)

    form = JobConfirmDeleteForm()
    return render_template("jobs/delete_confirm.html", job=job, form=form)

@job_bp.route("/<int:job_id>/delete", methods=["POST"]) # methods post: confirm deleted data from database 
@login_required
def delete(job_id: int):
    job = JobService.get_by_id(job_id)
    if job is None:
        abort(404)

    JobService.delete(job)
    flash(f"Job: '{job.job_title}' was deleted successfully.", "success")
    return redirect(url_for("jobs.index"))