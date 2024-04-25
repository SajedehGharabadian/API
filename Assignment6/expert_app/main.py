from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    yield db
    db.close()

@app.get("/")
def read_root():
   return{"message" : "University system API"}


@app.get("/student/", response_model=schemas.Student)
def read_students(student_id:int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    student_db = crud.create_student(db, student=student)
    return student_db

@app.delete("/del_student/{id}")
def delete_student(id:int, db:Session = Depends(get_db)):
    mes = crud.delete_student(db=db , student_id=id)
    return mes

@app.put("/students", response_model=schemas.Student)
def update_student(id:int, student: schemas.StudentCreate, db:Session = Depends(get_db)):
    db_student = crud.update_student(id=id, db=db, student=student)
    return db_student


#---------------Courses---------------------

@app.get("/courses/", response_model=schemas.Course)
def read_courses(course_id:int , db: Session = Depends(get_db)):
    course = crud.get_courses(db=db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.put("/courses", response_model=schemas.Course)
def update_course(id:int, course: schemas.CourseCreate, db:Session = Depends(get_db)):
    db_course = crud.update_course(id=id, db=db, student=course)
    return db_course


@app.delete("/del_course/{id}")
def delete_course(id:int, db:Session = Depends(get_db)):
    mes = crud.delete_course(db=db , course_id=id)
    return mes

@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, id:int, db: Session = Depends(get_db)):
    course_db = crud.create_course(db=db, id=id, course=course)
    return course_db