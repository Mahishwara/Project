import re
from typing import Optional

from pydantic import BaseModel, Field, EmailStr, field_validator
from pydantic.v1 import validator


class SObject(BaseModel):
    class Config:
        from_attributes = True

    id: int
    name: str = Field(..., min_length=1, max_length=100, description="Название, от 1 до 100 символов")
    description: str = Field(..., description="Описание")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес объекта, не более 200 символов")
    email: EmailStr = Field(..., description="Электронная почта объекта")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    category_id: int = Field(..., ge=1, description="ID категории объекта")


    @validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value


class SObjectAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Название, от 1 до 100 символов")
    description: str = Field(..., description="Описание")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес объекта, не более 200 символов")
    email: EmailStr = Field(..., description="Электронная почта объекта")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    category_id: int = Field(..., ge=1, description="ID категории объекта")


    @validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values
