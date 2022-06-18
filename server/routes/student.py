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
    Tags,
)

router = APIRouter()


@router.post("/create", response_description="Student data added into the database", tags=[Tags.student])
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


@router.put("/update/{student_id}")
async def update_student_data(student_id: str, student: UpdateStudentModel = Body(...), tags=[Tags.student]):
    student = jsonable_encoder(student.dict())
    new_student = await update_student(student_id, student)
    return ResponseModel(new_student, "Student Updated Successfuly")

@router.delete('/delete/{student_id}', tags=[Tags.student])
async def delete_student_data(student_id: str):
    await delete_student(student_id)
    return {'message': "Student Deleted Successfuly."}


@router.get('/retreive/{student_id}', status_code=200)
async def retreive_student_data(student_id: str):
    student = await retrieve_student(student_id)
    return ResponseModel(student, 'Fetched Requested Student Successfuly.')
