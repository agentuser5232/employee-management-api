from sqlalchemy.orm import Session

from .models import Employee
from .schemas import EmployeeCreate


def create_employee(db: Session, employee: EmployeeCreate):
    record = Employee(**employee.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_employees(db: Session):
    return db.query(Employee).all()
