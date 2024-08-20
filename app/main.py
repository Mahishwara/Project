import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.Object.router import router as routerObj
from app.Category.router import router as routerType
from app.pages.router import router as router_pages
from app.users.router import router as router_user
from app.reservations.router import router as router_reservation


app = FastAPI()


app.mount('/static', StaticFiles(directory='app/static'), 'static')


app.include_router(routerObj)
app.include_router(routerType)
app.include_router(router_user)
app.include_router(router_reservation)
app.include_router(router_pages)



if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=85, reload=True)
