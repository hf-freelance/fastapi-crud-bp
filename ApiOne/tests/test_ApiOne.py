import pytest

from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status
from bson import ObjectId

from ApiOne.db.models import ProductCollection, Product

async def test_items(client: AsyncClient, fastapi_app: FastAPI, db_conf):
    url = fastapi_app.url_path_for("read_all_items")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "products" in data


async def test_item_by_id(client: AsyncClient, fastapi_app: FastAPI, db_conf):
    url = fastapi_app.url_path_for("read_item", id="666194403d51ac1b83cdcdf6")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


async def test_health(client: AsyncClient, fastapi_app: FastAPI):
    """
    Checks the health endpoint.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    url = fastapi_app.url_path_for("health_check")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK


async def test_health_wrong(client: AsyncClient, fastapi_app: FastAPI):
    """
    Checks a wrong endpoint.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    response = await client.get("/wrong")
    assert response.status_code == status.HTTP_404_NOT_FOUND




"""


async def test_item_by_id(client: AsyncClient, fastapi_app: FastAPI, db_conf):
    url = fastapi_app.url_path_for("read_item", id="666194403d51ac1b83cdcdf6")
    response = await client.get(url)
    assert response != None


async def test_item_by_id_route(client: AsyncClient, fastapi_app: FastAPI, db_conf):
    response = await client.get("/api/item")
    assert response != None

async def test_item_by_id_wrong2(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("read_item_test")
    
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.anyio
async def test_item_by_id_wrong1(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("read_item_test_wrong")
    
    response = await client.get(url)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.anyio
async def test_item_by_id_wrong3(client: AsyncClient, fastapi_app: FastAPI) -> None:
    url = fastapi_app.url_path_for("read_item_test_wrongstr")
    
    response = await client.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

"""

