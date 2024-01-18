from sqlalchemy.orm import Session

import models, schema


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.Student):
    #fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, age=user.age, grade=user.year)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_stud(db: Session, user: schema.StudUpdate):
    db_stud = db.query(models.User).filter(models.User.id == user.id).first()
    if user.name != None:
        db_stud.name = user.name
    if user.age != None:
        db_stud.age = user.age
    if user.year != None:
        db_stud.grade = user.year
    db.commit()
    db.refresh(db_stud)
    return db_stud

def delete_stud(db: Session, user: schema.studDelete):
    db_stud = db.query(models.User).filter(models.User.id == user.id).first()
    db.delete(db_stud)
    db.commit()
    return db_stud


