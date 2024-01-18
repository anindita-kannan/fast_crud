from pydantic import BaseModel
from typing import Optional, Union

class StudentBase(BaseModel):
    id : int
    name : str
    age : int
    year : int

    

class Student(StudentBase):
    id : int
    name: str
    age : int
    year : int

    class Config:
        orm_mode = True


class StudUpdate(Student): 
    id: int
    name: Union[str, None]
    age: Union[int, None] 
    year: Union[int, None]

    class Config:
        orm_mode = True

class studDelete(BaseModel):
     id : int
     name: str
     age : int
     year : int