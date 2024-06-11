from fastapi import APIRouter

from routers.home.index import router

home_router = APIRouter()
home_router.include_router(router=router, tags=['home'])
