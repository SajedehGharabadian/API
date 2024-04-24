from sqlalchemy.orm import Session
import models, schemas
from fastapi import  HTTPException

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def create_student(db: Session, student: schemas.StudentCreate):
    db_student= models.Student(firstname=student.firstname, lastname=student.lastname, average=student.average, graduate=student.graduate)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student: schemas.StudentCreate,student_id:int):
    student_db = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student_db is None:
        raise HTTPException(status_code=404,detail="Student not found")
    
    student_db.firstname = student.firstname
    student_db.lastname = student.lastname
    student_db.average = student.average
    student_db.graduate = student.graduate

    return student_db

def delete_student(db: Session, student_id:int):
    student_db = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student_db is None:
        raise HTTPException(status_code=404,detail="Student not found")
    
    db.delete(student_db)
    db.commit()
    return "Student deleted"


def create_course(db: Session, id:int, course: schemas.CourseCreate):
    db_course = models.Course(name=course.name, unit=course.unit, owner_id=id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()



def update_course(db: Session, course: schemas.CourseCreate,course_id:int):
    course_db = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course_db is None:
        raise HTTPException(status_code=404,detail="Course not found")
    
    course_db.name = course.name
    course_db.unit = course.unit

    return course_db


def delete_course(db: Session, course_id:int):
    course_db = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course_db is None:
        raise HTTPException(status_code=404,detail="Student not found")
    
    db.delete(course_db)
    db.commit()
    return "Course deleted"

