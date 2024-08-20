from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, str_uniq, int_pk, str_null_true


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    description: Mapped[str_null_true]
    objects: Mapped[list["Object"]] = relationship("Object", back_populates="category")
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
