from app.dao.base import BaseDAO
from app.Object.models import Object


class ObjectDAO(BaseDAO):
    model = Object
