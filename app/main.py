import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from Object.router import router as routerObj
from Category.router import router as routerType
from pages.router import router as router_pages
from users.router import router as router_user
from reservations.router import router as router_reservation


app = FastAPI()
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)
app.mount('/static', StaticFiles(directory='/home/Mahishwara/Project/app/static'), 'static')


app.include_router(routerObj)
app.include_router(routerType)
app.include_router(router_user)
app.include_router(router_reservation)
app.include_router(router_pages)
