from fastapi import APIRouter, Depends, Response

from src.db.city_model import City, CityData, CityInfo

from .service import CityService

router = APIRouter(prefix="/City", tags=["City API"])


@router.post(
    "/add",
    response_model=City,
    description="Add a new city",
)
async def add_city(
    city_name: str,
    service: CityService = Depends(CityService),
) -> City:
    return service.add_city(city_name)


@router.delete(
    "/Delete",
    description="Delete a city",
)
async def delete_city(
    city_name: str,
    service: CityService = Depends(CityService),
) -> Response:
    service.delete_city(city_name)
    return Response(status_code=200)


@router.get(
    "/get_city_info",
    response_model=list[CityInfo] | CityInfo,
    description="Get information about a city",
)
async def get_city(
    city_name: str | None = None,
    service: CityService = Depends(CityService),
) -> list[CityInfo] | CityInfo:
    return service.get_city(city_name)


@router.get(
    "/find_nearest_cities",
    response_model=list[CityData] | CityData,
    description="find nearest city",
)
async def find_nearest_cities(
    latitude: float,
    longitude: float,
    service: CityService = Depends(CityService),
) -> list[CityData] | CityData:
    return service.find_nearest_cities(longitude, latitude)
