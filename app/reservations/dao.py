import datetime
from datetime import date

from sqlalchemy import select, and_


from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.reservations.models import Reservation



class ReservationDAO(BaseDAO):
    model = Reservation

    async def check_new_reservation(date_from: date, count_days: int, name: str, object_id: int):
        if date_from < date.today():
            return 'Нельзя забронировать в прошлом'
        async with async_session_maker() as session:
            date_to = date_from + datetime.timedelta(days=count_days)
            query = select(Reservation).filter_by(object_id=object_id).where(and_(Reservation.date_from < date_to,
                                                                                  Reservation.date_to > date_from))
            result = await session.execute(query)
            intersections = result.scalars().all()
            res = ''
            if intersections:
                res += 'Даты уже забронированы:'
                for intersection in intersections:
                    res += f' {max(date_from, intersection.date_from)} - {min(intersection.date_to, date_to)},'
                return res[:-1]
            return date_to
