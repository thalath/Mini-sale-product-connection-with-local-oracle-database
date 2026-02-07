from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

from app.models.jobs import Job

class JobCreateForm(FlaskForm):
    job_title = StringField(
        "Enter Job Title",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the job title"}
    )
    
    min_salary = FloatField(
        "Minimum",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter minimum Salary"}
    )
    
    max_salary = FloatField(
        "Maximum Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the maximum Salary"}
    )
    
    submit = SubmitField("Save")

    
class JobEditForm(FlaskForm):
    job_title = StringField(
        "Enter Job Title",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the job title"}
    )
    
    min_salary = FloatField(
        "Minimum",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter minimum Salary"}
    )
    
    max_salary = FloatField(
        "Maximum Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter the maximum Salary"}
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_job: Job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_job = original_job
        
class JobConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")
        