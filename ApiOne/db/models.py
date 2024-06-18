from typing import Union, List, Optional
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from pydantic import ConfigDict, BaseModel, Field, EmailStr


PyObjectId = Annotated[str, BeforeValidator(str)]

class Product(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None) 
    name: str = Field(...)
    price: float = Field(...)
    is_offer: bool = Field(...)

class ProductCollection(BaseModel):
    products: List[Product]
