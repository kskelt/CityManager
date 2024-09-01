from fastapi import APIRouter

from .city.router import router as city_router


router = APIRouter()
router.include_router(city_router)