from typing import Union, List, Optional

from typing_extensions import Annotated
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator
from importlib import metadata

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, UJSONResponse

import motor.motor_asyncio
from bson import ObjectId

from ApiOne.web.router import api_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="FastApi MongoDB Boilerplate 2024",
        version=metadata.version("ApiOne"),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")

    return app

