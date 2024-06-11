from fastapi import APIRouter
from langserve import add_routes

from providers.groq import GroqProvider

router = APIRouter(prefix="/llm")

groq_provider = GroqProvider()
groq_chain = groq_provider.base_chain()

add_routes(
    router,
    groq_chain,
    path="/groq"
)
