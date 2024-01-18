from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
import crud
import schema
from pydantic import BaseModel
from typing import Optional,List

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# class Student(BaseModel):
#     id: int
#     name : str
#     age : int
#     year : int

#     class Config:
#         orm_mode = True

# class Student_response(Student):
#     id: int
#     name : str
#     age : int
#     year : int
    

#     class Config:
#         orm_mode = True


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message":"hello"}


# def create_user(db: Session, user: Student, id:int):
#     db_user = models.User(id=user.id)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


@app.post("/users/", response_model=List[schema.Student])
def create_user(user: schema.Student, id: int,db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Student already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    items=db.query(models.User).all()
    return {"items": items}


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user =crud.get_user_by_id(db, id=user_id)
   
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {user_id : db_user}


@app.put("/students/")
def update(user: schema.StudUpdate, db: Session = Depends(get_db)):
    return crud.update_stud(db=db, user=user )

@app.delete("/students/")
def delete_user(user: schema.studDelete, db: Session = Depends(get_db)):
    return crud.delete_stud(db=db, user=user)

