from sqlalchemy import ForeignKey, String, Integer, Text
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

# создаем модель таблицы объектов бронирования
class Object(Base):
    __tablename__ = 'objects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    address: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(25), nullable=False)
    photo: Mapped[str] = mapped_column(Text, nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
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
