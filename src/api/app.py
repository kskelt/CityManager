from typing import Dict

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .router import router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/")
def root() -> Dict[str, str]:
    """Return the content of the application's root page.

    Returns:
        dict: Dictionary with the contents of the root page.
    """
    return {"DataBase": "0.0.1"}
