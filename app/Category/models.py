from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(150))
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, category_name={self.name!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            'name': self.name,
            "description": self.description}
