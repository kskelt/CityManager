from pydantic import BaseModel, ConfigDict


class CityData(BaseModel):
    name: str | None


class CityInfo(CityData):
    latitude: float | None
    longitude: float | None


class City(CityInfo):
    id: int
    model_config = ConfigDict(from_attributes=True)
