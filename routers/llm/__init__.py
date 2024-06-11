from fastapi import APIRouter

from routers.llm import groq

llm_router = APIRouter()
llm_router.include_router(router=groq.router)
