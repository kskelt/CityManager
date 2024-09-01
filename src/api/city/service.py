import requests
from bs4 import BeautifulSoup
from fastapi import Depends, HTTPException, status
from sqlalchemy import select

from src.db import tables
from src.db.city_model import City, CityInfo
from src.db.database import Session, get_session
from src.utils.city_utils import haversine


class CityService:
    def __init__(
        self,
        session: Session = Depends(get_session),  # type: ignore
    ) -> None:
        self.session = session

    # Метод для получения координат города
    def get_city_coordinates(self, city_name: str):
        url = "https://time-in.ru/coordinates/russia"

        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Город {city_name} не найден на сайте time-in.ru",
            )

        soup = BeautifulSoup(response.text, "html.parser")

        city_items = soup.find_all("li")

        for item in city_items:
            city_tag = item.find("a", class_="coordinates-items-left")
            if city_tag and city_tag.text.strip().lower() == city_name.lower():
                coordinates_tag = item.find("div", class_="coordinates-items-right")
                if coordinates_tag:
                    coord_text = coordinates_tag.text.strip()
                    lat_str, lon_str = coord_text.split(",")
                    lat, lon = float(lat_str.strip()), float(lon_str.strip())
                    return lat, lon

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Координаты для города {city_name} не найдены",
        )

    # Метод для добавления нового города в базу данных
    def add_city(self, city_name: str) -> City:
        stmt = select(tables.City).where(tables.City.name == city_name)
        existing_city = self.session.execute(stmt).scalar()
        if existing_city:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Город уже существует"
            )
        lat, lon = self.get_city_coordinates(city_name)

        city_info = CityInfo(name=city_name, latitude=lat, longitude=lon)

        new_city = tables.City(
            name=city_info.name,
            latitude=city_info.latitude,
            longitude=city_info.longitude,
        )
        self.session.add(new_city)
        self.session.commit()

        return new_city

    # Метод для удаления города из базы данных
    def delete_city(self, city_name: str) -> City:
        stmt = select(tables.City).where(tables.City.name == city_name)
        city = self.session.execute(stmt).scalar()
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Город не найден"
            )
        self.session.delete(city)
        self.session.commit()
        return city

    # Метод для получения информации о городе
    def get_city(self, city_name: str | None) -> CityInfo:
        if city_name is None:
            stmt = select(tables.City)
            city = self.session.execute(stmt).scalars().all()
        else:
            stmt = select(tables.City).where(tables.City.name == city_name)
            city = self.session.execute(stmt).scalar()
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Город не найден"
            )
        return city

    # Метод для поиска ближайших городов к точке
    def find_nearest_cities(self, longitude, latitude, limit=2):
        if not (-90 <= latitude <= 90):
            raise ValueError("Широта должна быть в диапазоне от -90 до 90 градусов.")

        if not (-180 <= longitude <= 180):
            raise ValueError("Долгота должна быть в диапазоне от -180 до 180 градусов.")

        stmt = select(tables.City)
        cities = self.session.execute(stmt).scalars().all()
        cities_with_distances = [
            (city, haversine(latitude, longitude, city.latitude, city.longitude))
            for city in cities
        ]
        cities_with_distances.sort(key=lambda x: x[1])
        nearest_cities = [
            city for city, distance in cities_with_distances[1 : limit + 1]
        ]
        return nearest_cities
