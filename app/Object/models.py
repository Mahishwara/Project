from sqlalchemy import ForeignKey, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk, str_null_true


# создаем модель таблицы объектов бронирования
class Object(Base):
    __tablename__ = 'objects'

    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str_null_true]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str_uniq]
    phone_number: Mapped[str_uniq]
    photo: Mapped[str] = mapped_column(Text, nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    category: Mapped["Category"] = relationship("Category", back_populates="objects")
    reservations: Mapped["Reservation"] = relationship("Reservation", back_populates="object")
    extend_existing = True

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.name}",
                f'description={self.description}')

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'name': self.name,
            "description": self.description,
            'adress': self.address,
            'email': self.email,
            'phone_number': self.phone_number,
            'category_id': self.category_id,
        }
