from app.dao.base import BaseDAO
from app.Category.models import Category


class CategoryDAO(BaseDAO):
    model = Category