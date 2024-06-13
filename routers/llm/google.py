from fastapi import APIRouter
from langserve import add_routes

from providers.google import GoogleProvider

router = APIRouter(prefix="/llm")

google_provider = GoogleProvider()
google_chain = google_provider.basic_chat_chain()

add_routes(
    router,
    google_chain,
    path="/google"
)
