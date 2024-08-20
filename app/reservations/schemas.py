from datetime import date

from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import Date


class SReservation(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(..., description='Название для понимания')
    date_from: date = Field(..., description="Дата начала бронирования")
    date_to: date = Field(..., description="Дата окончания бронирования")
    object_id: int = Field(..., ge=1, description="ID объекта, который бронирется")
    user_id: int = Field(..., ge=1, description="ID пользоателя, который бронирует")


class SReservationAdd(BaseModel):
    name: str = Field(..., description='Название для понимания')
    date_from: date = Field(..., description="Дата начала бронирования")
    date_to: date = Field(..., description="Дата окончания бронирования")
    object_id: int = Field(..., ge=1, description="ID объекта, который бронирется")
    user_id: int = Field(..., ge=1, description="ID пользоателя, который бронирует")



class SReservationCheck(BaseModel):
    name: str = Field(..., description='Название для понимания')
    date_from: date = Field(..., description="Дата начала бронирования")
    count_days: int = Field(..., description="Количество дней")
    object_id: int = Field(..., ge=1, description="ID объекта, который бронирется")