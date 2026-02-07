
from typing import List, Optional
from extensions import db
from app.models.jobs import Job

class JobService:
    
    @staticmethod
    def get_all() -> List[Job]:
        return Job.query.order_by(Job.job_id.asc()).all()
    
    @staticmethod
    def get_by_id(job_id) -> Optional[Job]:
        return Job.query.get(job_id)
    
    @staticmethod
    def create(data: dict) -> Job:
        job = Job(
            job_title = data["job_title"],
            min_salary = data["min_salary"],
            max_salary  = data["max_salary"]
        )
        
        db.session.add(job)
        db.session.commit()
        return job
    
    @staticmethod
    def update(job: Job, data: dict) -> Job:
        job.job_title = data["job_title"]
        job.min_salary = data["min_salary"]
        job.max_salary = data["max_salary"]

        db.session.commit()
        return job

    @staticmethod
    def delete(job: Job) -> None:
        db.session.delete(job)
        db.session.commit()