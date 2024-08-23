from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import datetime


class Reservation(Base):
    __tablename__ = 'reservations'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    date_from: Mapped[datetime.datetime]
    date_to: Mapped[datetime.datetime]
    object_id: Mapped[int] = mapped_column(ForeignKey("objects.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}",
                f"name={self.name}"
                f"date_from={self.date_from}",
                f"date_to={self.date_to}",
                f"object_id={self.object_id}",
                f"user_id={self.date_from}")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'name': self.name,
            'date_from': self.date_from,
            "date_to": self.date_to,
            'object_id': self.object_id,
            'user_id': self.user_id,
        }
