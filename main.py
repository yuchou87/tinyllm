from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.home import home_router

app = FastAPI(
    title="lark_chat_bot Server",
    version="1.0",
    description="A webhook chat bot",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(router=home_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
