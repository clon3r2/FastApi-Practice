from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/create", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


@router.put('/update/{student_id}')
async def update_student_data(student_id: str, student: UpdateStudentModel= Body(...)):
    print('student: ', student)
    student = jsonable_encoder(student)
    print('encoded student: ', student)
    new_student = await update_student(student_id, student)
    print('new student: ', new_student)
    return ResponseModel(new_student, "Student Updated Successfuly")