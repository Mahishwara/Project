from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.Category.router import get_all_categories
from app.Object.router import get_all_objects, get_object
from app.reservations.rb import RBReservation
from app.reservations.router import get_reservations
from app.users.router import get_me

router = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/objects')
async def get_objects_html(request: Request, objects=Depends(get_all_objects)):
    return templates.TemplateResponse(name='objects.html', context={'request': request, 'objects': objects})


@router.get('/')
async def get_objects_html(request: Request, categories=Depends(get_all_categories)):
    return templates.TemplateResponse(name='categories.html', context={'request': request, 'categories': categories})


@router.get('/objects/{object_id}')
async def get_object_html(request: Request, object=Depends(get_object)):
    return templates.TemplateResponse(name='object.html',
                                      context={'request': request, 'obj': object})


@router.get('/profile')
async def get_my_profile(request: Request, profile=Depends(get_me)):
    reservations = await get_reservations(RBReservation(user_id=profile.id))
    return templates.TemplateResponse(name='profile.html', context={'request': request, 'profile': profile,
                                                                    'reservations': reservations})


@router.get('/register')
async def get_register_html(request: Request):
    return templates.TemplateResponse(name='register_form.html', context={'request': request})


@router.get('/login')
async def get_login_html(request: Request):
    return templates.TemplateResponse(name='login_form.html', context={'request': request})


@router.get('/reservation')
async def get_reservation_html(request: Request, object=Depends(get_object)):
    return templates.TemplateResponse(name='reservation.html',
                                      context={'request': request, 'obj': object})

@router.get('/')
async def get_base(request: Request):
    return templates.TemplateResponse(name='base.html', context={'request': request})