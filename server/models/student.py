import enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Tags(enum.Enum):
    student: str = 'student'
    

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Alireza Delkhahi",
                "email": "alireza@gmail.com",
                "course_of_study": "Fastapi course",
                "year": 4,
                "gpa": 1.0,
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Alireza Delkhahi",
                "email": "alireza@gmail.com",
                "course_of_study": "Fastapi course",
                "year": 4,
                "gpa": 1.0,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}