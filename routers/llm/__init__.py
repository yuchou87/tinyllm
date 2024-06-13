from fastapi import APIRouter

from routers.llm import groq, google

llm_router = APIRouter()
llm_router.include_router(router=groq.router)
llm_router.include_router(router=google.router)
