from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length
from app.models.employees import Employee

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
]

REMARK_CHOICES = [
    ("Excellent", "Excellent"),
    ("Good", "Good"),
    ("Normal", "Normal")
]


class EmployeeCreateForm(FlaskForm):
    employeeName = StringField(
        "Employee Name",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Enter New Employee's Name"},
    )
    
    gender = SelectField(
        "Select Gender",
        choices=GENDER_CHOICES,
        default="Male"
    )
    
    birthdate = DateField(
        "Birth Date",
        format="%Y-%m-%d",
        validators=[DataRequired()]
    )
    
    JOB_ID = IntegerField(
        "Enter JOB_ID",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter JOB_ID references from job table"}
    )
    
    ADDRESS = StringField(
        "Enter Address",
        render_kw={"placeholder": "Enter address. e.g. #123, dev Street..."}
    )
    
    PHONE = StringField(
        "Enter Phone number",
        validators=[DataRequired(), Length(max=15)],
        render_kw={"placeholder": "Enter your phone. make that numberic are unique"}
    )
    
    SALARY = FloatField(
        "Enter Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Salary references from JOB table"}
    )
    
    REMARK = SelectField(
        "Select Remark",
        choices=REMARK_CHOICES,
        default="Normal"
    )
    
    PHOTO = FileField(
        "Profile Photo",
        validators=[FileAllowed(['jpg', 'jpeg', 'png'], "Image only!")]
    )
    
    submit = SubmitField("Save")
    
class EmployeeEditForm(FlaskForm):
    employeeName = StringField(
        "Employee Name",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Enter New Employee's Name"},
    )
    
    gender = SelectField(
        "Select Gender",
        choices=GENDER_CHOICES,
        default="Male"
    )
    
    birthdate = DateField(
        "Birth Date",
        format="%Y-%m-%d",
        validators=[DataRequired()]
    )
    
    JOB_ID = IntegerField(
        "Enter JOB_ID",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter JOB_ID references from job table"}
    )
    
    ADDRESS = StringField(
        "Enter Address",
        render_kw={"placeholder": "Enter address. e.g. #123, dev Street..."}
    )
    
    PHONE = StringField(
        "Enter Phone number",
        validators=[DataRequired(), Length(max=15)],
        render_kw={"placeholder": "Enter your phone. make that numberic are unique"}
    )
    
    SALARY = FloatField(
        "Enter Salary",
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter Salary references from JOB table"}
    )
    
    REMARK = SelectField(
        "Select Remark",
        choices=REMARK_CHOICES,
        default="Normal"
    )
    
    PHOTO = FileField(
        "Profile Photo",
        validators=[FileAllowed(['jpg', 'jpeg', 'png'], "Image only!")]
    )
    
    submit = SubmitField("Update")
    
    def __init__(self, original_emp: Employee, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_emp = original_emp
    
class EmployeeConfirmDeleteForm(FlaskForm):
    submit = SubmitField("Confirm Delete")
