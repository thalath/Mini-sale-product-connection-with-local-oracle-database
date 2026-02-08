from extensions import db
from sqlalchemy import Identity

class Employee(db.Model):
    __tablename__ ="EMPLOYEES"
    
    employeeid = db.Column(db.Integer,  primary_key=True)
    employeename = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(6))
    birthdate = db.Column(db.DATE)
    JOB_ID = db.Column(db.Integer)
    ADDRESS = db.Column(db.String(150))
    PHONE = db.Column(db.String(15), unique=True, nullable=False)
    SALARY = db.Column(db.Float)
    REMARK = db.Column(db.String(50))
    PHOTO = db.Column(db.BLOB)
    
    def __repr__(self) -> set[str]:
        return f"<Employee '{self.employeename}'>"
