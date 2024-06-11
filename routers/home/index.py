from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index_page():
    return "index"


@router.get("/health")
def health_check():
    return {"status": "ok"}
