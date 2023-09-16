from enum import Enum

from pydantic import BaseModel, EmailStr, field_validator


class SubjectEnum(str, Enum):
    english = "English"
    math = "Math"
    science = "Science"
    art = "Art"


class Person(BaseModel):
    first_name: str
    last_name: str


class Student(Person):
    """
    Some ways a student is different. A student will always have a number for their email address
    A student attends classes
    All students must take english and math and at least one other subject
    """

    email: EmailStr
    subjects: list[SubjectEnum]

    @field_validator("subjects")
    @classmethod
    def required_subjects(cls, subs: list):
        assert all([SubjectEnum.math, SubjectEnum.english]) in subs, "students must take math and english"
        assert len(subs) > 2, "students must take at least 2 subjects"


student = Student(
    first_name="first",
    last_name="last",
    email="student@example.com",
    subjects=[SubjectEnum.math, SubjectEnum.english, SubjectEnum.science],
)
