from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from Category.router import get_all_categories
from Object.router import get_all_objects, get_object
from reservations.rb import RBReservation
from reservations.router import get_reservations
from users.router import get_me
from datetime import datetime

router = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='/home/Mahishwara/Project/app/templates')

@router.get('/objects')
async def get_objects_html(request: Request, objects=Depends(get_all_objects)):
    return templates.TemplateResponse('objects.html', context={'request': request, 'objects': objects})


@router.get('/')
async def get_categories_html(request: Request, categories=Depends(get_all_categories)):
    return templates.TemplateResponse('categories.html', context={'request': request, 'categories': categories})


@router.get('/objects/{object_id}')
async def get_object_html(request: Request, object=Depends(get_object)):
    return templates.TemplateResponse('object.html',
                                      context={'request': request, 'obj': object})


@router.get('/profile')
async def get_my_profile(request: Request, profile=Depends(get_me)):
    reservations = await get_reservations(RBReservation(user_id=profile.id))
    return templates.TemplateResponse('profile.html', context={'request': request, 'profile': profile,
                                                                    'reservations': reservations, 'today': datetime.now()})


@router.get('/register')
async def get_register_html(request: Request):
    return templates.TemplateResponse('register_form.html', context={'request': request})


@router.get('/login')
async def get_login_html(request: Request):
    return templates.TemplateResponse('login_form.html', context={'request': request})


@router.get('/reservation')
async def get_reservation_html(request: Request, object=Depends(get_object)):
    return templates.TemplateResponse('reservation.html',
                                      context={'request': request, 'obj': object})
