from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.home import home_router
from routers.llm import llm_router

app = FastAPI(
    title="tiny llm server",
    version="1.0",
    description="a tiny llm server",
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
app.include_router(router=llm_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
