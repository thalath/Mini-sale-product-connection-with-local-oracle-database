from extensions import db
from typing import List, Optional
from app.models.employees import Employee
from werkzeug.datastructures import FileStorage

class EmployeeService:
    
    @staticmethod
    def get_all() -> List[Employee]:
        return Employee.query.order_by(Employee.employeeid.asc()).all()
    
    @staticmethod
    def get_by_id(employee_id: int) -> Optional[Employee]:
        return Employee.query.get(employee_id)

    @staticmethod
    def create(data: dict, photo: FileStorage | None) -> Employee:
        emps = Employee(
            employeename = data["employeename"],
            gender = data.get("gender", "Male"),
            birthdate = data["birthdate"] or "DatePicker not found!",
            JOB_ID = data["JOB_ID"],
            ADDRESS = data.get("ADDRESS") or "",
            PHONE = data["PHONE"],
            SALARY = data.get("SALARY") or 0.00,
            REMARK = data.get("REMARK", "Normal")
        )
        
        if photo:
            Employee.PHOTO = photo.read()
        
        db.session.add(emps)    
        db.session.commit()
        return emps
    
    @staticmethod
    def update(employee: Employee, data: dict, photo: FileStorage | None) -> Employee:
        employee.employeename = data["employeename"]
        employee.gender = data["gender"]
        employee.birthdate = data["birthdate"]
        employee.JOB_ID = data["JOB_ID"]
        employee.ADDRESS = data["ADDRESS"]
        employee.PHONE = data["PHONE"]
        employee.SALARY = data["SALARY"]
        employee.REMARK = data["REMARK"]
        
        if photo and photo.filename != "":
            employee.PHOTO = photo.read()
        else:
            employee.PHOTO = None
            
        db.session.commit()
        return employee
    
    @staticmethod
    def delete(employee: Employee):
        db.session.delete(employee)
        db.session.commit()
