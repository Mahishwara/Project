from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.database import Base, int_pk


class Reservation(Base):
    __tablename__ = 'reservations'

    id: Mapped[int_pk]
    name: Mapped[str]
    date_from: Mapped[date]
    date_to: Mapped[date]
    object_id: Mapped[int] = mapped_column(ForeignKey("objects.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    object: Mapped["Object"] = relationship("Object", back_populates="reservations")
    user: Mapped["User"] = relationship("User", back_populates="reservations")
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