from datetime import date

from fastapi import APIRouter, Depends

from reservations.dao import ReservationDAO
from reservations.rb import RBReservation
from reservations.schemas import SReservation, SReservationAdd, SReservationCheck

router = APIRouter(
    prefix='/reservations',
    tags=['Бронирование']
)

@router.get('/', summary="Получить все бронирования")
async def get_reservations(request_body: RBReservation = Depends()) -> list[SReservation]:
    return await ReservationDAO.get_all_objects(**request_body.to_dict())


@router.get("/{reservation_id}", summary="Получить одно бронирование по ID")
async def get_reservation(reservation_id: int) -> SReservation | dict:
    res = await ReservationDAO.get_object(id=reservation_id)
    if res is None:
        return {'': 'Бронирование с данными ID не найдено!'}
    return res


@router.post("/add", summary="Добавить новое бронирование")
async def add_new_object(reservation: SReservationAdd) -> dict:
    check = await ReservationDAO.add(**reservation.dict())
    if check:
        return {"message": "Бронирование успешно добавленo!"}
    else:
        return {"message": "Ошибка при добавлении бронирования!"}


@router.delete("/dell", summary='Удалить бронирование')
async def dell_by_id(request_body: RBReservation = Depends()) -> dict:
    check = await ReservationDAO.delete(**request_body.to_dict())
    if check:
        return {"message": "Бронирование успешно удалено!"}
    else:
        return {"message": "Ошибка при удалении бронирования!"}


@router.post("/check", summary='Проверить новое бронирование')
async def check(reservation: SReservationCheck) -> dict:
    check = await ReservationDAO.check_new_reservation(**reservation.dict())
    if type(check) == str:
        return {"detail": check}
    else:
        return {'ok': True, 'data': {'name': reservation.name, 'date_from': reservation.date_from,
                'date_to': check, 'object_id': reservation.object_id}}
