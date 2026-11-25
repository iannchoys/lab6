"""FastAPI-приложение с использованием Pydantic-схем."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="Pydantic API",
    description="Демонстрация проверки и обработки данных",
    version="1.0.0",
)


class StudentCreate(BaseModel):
    """Схема входящих данных студента."""

    full_name: str = Field(min_length=5, max_length=100)
    group: str = Field(min_length=3, max_length=20)
    variant: int = Field(ge=1, le=10)


class StudentResponse(StudentCreate):
    """Схема ответа с идентификатором студента."""

    id: int = Field(ge=1)


# Временное хранилище студентов.
students: list[StudentResponse] = []


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=201,
)
def create_student(student: StudentCreate) -> StudentResponse:
    """Создаёт студента после проверки входящих данных."""

    new_student = StudentResponse(
        id=len(students) + 1,
        full_name=student.full_name,
        group=student.group,
        variant=student.variant,
    )

    students.append(new_student)

    return new_student


@app.get(
    "/students",
    response_model=list[StudentResponse],
)
def get_students() -> list[StudentResponse]:
    """Возвращает список всех студентов."""
    return students


@app.get(
    "/students/{student_id}",
    response_model=StudentResponse,
)
def get_student(student_id: int) -> StudentResponse:
    """Возвращает одного студента по идентификатору."""

    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Студент не найден",
    )
