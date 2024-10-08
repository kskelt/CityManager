# CityManager

## 📄 Описание

Этот проект представляет собой HTTP API, с помощью которого можно: 
 - добавлять/удалять в хранилище информацию о городах запрашивать информацию о городах из хранилища;
 - по заданным широте и долготе точки выдавать 2 ближайших к ней города из присутствующих в хранилище. 
При запросе к API на добавление нового города клиент указывает только название города, а в хранилище добавляются также координаты города. Данные о координатах можно получать из любого внешнего API.

- **FastAPI** для обработки API-запросов.
- **SQLAlchemy** для работы с базой данных.
- **BeautifulSoup** для парсинга HTML-страниц.

## 🛠 Требования

- **Python 3.12**
- **PDM**
- **PostgreSQL**

## 🚀 Установка

1. Убедитесь, что у вас установлен **Python 3.12** и **PDM**. Если PDM не установлен, выполните команду:

    ```
    python3 -m pip install pdm
    ```
2. Клонируйте репозиторий и перейдите в директорию проекта:

    ```
    git clone <repository_url>
    cd <project_name>
    ```

3. Установите зависимости проекта с помощью PDM:

    ```
    pdm install
    ```

4. Создайте файл .env в корне проекта и добавьте в него настройки конфигурации, такие как параметры подключения к базе данных.

## ▶️ Запуск проекта
1. С использованием PDM
Для запуска приложения с помощью PDM, выполните:

    ```
    pdm run uvicorn src.api.app:app --reload
    ```
2. С использованием Python
Для запуска приложения с помощью Python, выполните:
    ```
    pip install -r requirements.txt
    ```

    ```
    python3 -m uvicorn src.api.app:app --reload
    ```
    или
    ```
    python3 __main__.py
    ```

Приложение будет доступно по адресу http://127.0.0.1:8000.

## 📊 Миграции базы данных
Для управления миграциями используется Alembic. Чтобы создать новую миграцию и применить её, выполните следующие шаги:

Создание новой миграции:

    ```
    pdm run alembic revision --autogenerate -m "описание миграции"
    ```
Применение миграций:

    ```
    pdm run alembic upgrade head
    ```