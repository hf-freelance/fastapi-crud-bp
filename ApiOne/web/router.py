from fastapi.routing import APIRouter
from fastapi import status

from ApiOne.db.conf import db_conf, client
from ApiOne.db.models import ProductCollection, Product

from bson import ObjectId

api_router = APIRouter()

@api_router.get("/")
async def health_check():
    return {"Boilerplate": "FastAPI / Docker / MongoDB"}

@api_router.get("/items",
    response_description="List all products",
    response_model=ProductCollection,
    response_model_by_alias=False,
)
async def read_all_items():
    product_collection=db_conf.get_collection("product")
    return ProductCollection(products=await product_collection.find().to_list(10))

@api_router.get("/items/{id}",
    response_description="Fetch one product",
    response_model=Product,
    response_model_by_alias=False,
)
async def read_item(id: str):
    product_collection=db_conf.get_collection("product")
    return await product_collection.find_one(ObjectId(id))

@api_router.get("/item",
    response_description="Fetch one product",
    response_model=Product,
    response_model_by_alias=False,
)
async def read_item_test():
    id="666194643d51ac1b83cdcdf8"
    product_collection=db_conf.get_collection("product")
    res = await product_collection.find_one(ObjectId(id))
    if res["name"] == "ballon":
        return res
    return None
    

    """
    
        return await product_collection
    """
    """
        @app.get("/")
    async def read_root():
        return {"Boilerplate": "FastAPI / MongoDB"}

    @app.get("/items",
        response_description="List all products",
        response_model=ProductCollection,
        response_model_by_alias=False,
    )
    async def read_all_items():
        return ProductCollection(products=await product_collection.find().to_list(10))

    @app.get("/items/{id}",
        response_description="Fetch one product",
        response_model=Product,
        response_model_by_alias=False,
    )
    async def read_item(id: str):
        return await product_collection.find_one(ObjectId(id))

    @app.post(
        "/items",
        response_description="Add new product",
        response_model=Product,
        status_code=status.HTTP_201_CREATED,
        response_model_by_alias=False,
    )
    async def create_student(product: Product = Body(...)):
        new_product = await product_collection.insert_one(
            product.model_dump(by_alias=True, exclude=["id"])
        )
        created_product = await product_collection.find_one(
            {"_id": new_product.inserted_id}
        )
        return created_product


    @app.put("/items/{item_id}")
    def update_item(item_id: int, p: Product):
        return {"item_name": p.name, "item_id": item_id}
    """


