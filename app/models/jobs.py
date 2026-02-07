from extensions import db
from sqlalchemy import Identity, CheckConstraint
from sqlalchemy.orm import validates

class Job(db.Model):
    __tablename__ = "JOBS"
    job_id = db.Column(db.Integer, Identity(start=1), primary_key=True)
    job_title = db.Column(db.String(50),unique=True, nullable=False)
    min_salary = db.Column(db.Float, nullable=False)
    max_salary = db.Column(db.Float, nullable=False)
    
    __table_args__ = (
        CheckConstraint("min_salary < max_salary"),
    )
    
    @validates("min_salary", "max_salary")
    def validate_salary(self, key, value):
        if key == "min_salary" and self.max_salary is not None:
            if value >= self.max_salary:
                raise ValueError("min_salary must be less than max_salary")

        if key == "max_salary" and self.min_salary is not None:
            if self.min_salary >= value:
                raise ValueError("max_salary must be greater than min_salary")

        return value