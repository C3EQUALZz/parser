from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status

router = APIRouter(
    tags=['Wildberries parser handlers'],
    prefix="wildberries",
    route_class=DishkaRoute
)


@router.get(
    path="/{product_name}/",
    status_code=status.HTTP_200_OK,
    description='Get all products from wildberries by name which user provide'
)
async def get_products_by_name(product_name: str):
    ...


@router.get(
    path="/{article}/",
    status_code=status.HTTP_200_OK,
    description='Get product by article from wildberries which user provide'
)
async def get_product_by_id(article: str):
    ...


@router.get(
    path="/{category_name}/",
    status_code=status.HTTP_200_OK,
    description='Get all products from category wildberries which user provide'
)
async def get_products_by_category(category_name: str):
    ...


@router.get(
    path="/{brand_name}/",
    status_code=status.HTTP_200_OK,
    description='Get all products from brand'
)
async def get_products_by_brand(brand_name: str):
    ...
