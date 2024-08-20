import shutil

from fastapi import APIRouter, Depends, UploadFile

from app.Object.dao import ObjectDAO
from app.Object.rb import RBObject
from app.Object.schemas import SObject, SObjectAdd
from app.users.dependencies import get_current_admin_user
from app.users.models import User

router = APIRouter(
    prefix='/object',
    tags=['Объекты аренды']
)


@router.get("/", summary="Получить все объекты бронирования")
async def get_all_objects(request_body: RBObject = Depends()) -> list[SObject]:
    return await ObjectDAO.get_all_objects(**request_body.to_dict())


@router.get("/{}", summary="Получить один объект по ID")
async def get_object(object_id: int) -> SObject | dict:
    res = await ObjectDAO.get_object(id=object_id)
    if res is None:
        return {'message': f'Объект с данными ID не найден!'}
    return res


@router.post("/add/", summary='Добавить новый объект аренды')
async def add_new_object(object: SObjectAdd, user_data: User = Depends(get_current_admin_user)) -> dict:
    check = await ObjectDAO.add(**object.dict())
    if check:
        return {"message": "Объект успешно добавлен!", "object": object}
    else:
        return {"message": "Ошибка при добавлении объекта!"}


@router.delete("/dell/{}", summary='Удалить объект аренды')
async def dell_by_id(object_id: int, user_data: User = Depends(get_current_admin_user)) -> dict:
    check = await ObjectDAO.delete(id=object_id)
    if check:
        return {"message": f"Объект с ID {object_id} удален!"}

    else:
        return {"message": "Ошибка при удалении объекта!"}


@router.post('/add_photo')
async def add_object_photo(file: UploadFile, image_name: int, user_data: User = Depends(get_current_admin_user)):
    with open(f"app/static/images/{image_name}.webp", "wb+") as photo_obj:
        shutil.copyfileobj(file.file, photo_obj)