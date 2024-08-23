from fastapi import APIRouter, Depends

from Category.dao import CategoryDAO
from Category.rb import RBCategory
from Category.schemas import SCategory, SCategoryAdd, SCategoryUpd
from users.dependencies import get_current_admin_user
from users.models import User

router = APIRouter(
    prefix='/categories',
    tags=['Категории объектов']
)


@router.get("/", summary="Получить все категории объектов")
async def get_all_categories(request_body: RBCategory = Depends()) -> list[SCategory]:
    return await CategoryDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить одну категорию по ID")
async def get_category_by_id(category_id: int) -> SCategory | dict:
    res = await CategoryDAO.get_object(id=category_id)
    if res is None:
        return {'message': 'Категория с данным ID не найдена!'}
    return res


@router.post("/add", summary='Добавить новую категорию')
async def register_category(category: SCategoryAdd, user_data: User = Depends(get_current_admin_user)) -> dict:
    check = await CategoryDAO.add(**category.dict())
    if check:
        return {"message": "Категория успешно добавлена!", "category": category}
    else:
        return {"message": "Ошибка при добавлении категории!"}


@router.put("/update", summary='Изменить описание типа')
async def update_category(category: SCategoryUpd, user_data: User = Depends(get_current_admin_user)) -> dict:
    check = await CategoryDAO.update(filter_by={'category_name': category.category_name},
                                   category_description=category.category_description)
    if check:
        return {"message": "Описание категории успешно обновлено!", "category": category}
    else:
        return {"message": "Ошибка при обновлении описания категории!"}


@router.delete("/delete/{category_id}")
async def delete_category(request_body: RBCategory = Depends(), user_data: User = Depends(get_current_admin_user)) -> dict:
    check = await CategoryDAO.delete(**request_body.to_dict())
    if check:
        return {"message": "Категория(и) успешно удалена(ы)!"}
    else:
        return {"message": "Ошибка при удалении категории(й)!"}
