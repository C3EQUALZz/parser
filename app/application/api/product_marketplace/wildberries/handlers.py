from typing import List

from fastapi import (
    APIRouter,
    HTTPException,
)
from starlette import status

from app.application.api.error_schemas import ErrorSchema
from app.application.api.product_marketplace.wildberries.schemas import (
    ProductMarketPlaceRequestSchema,
    ProductMarketPlaceResponseSchema,
)
from app.application.api.product_marketplace.wildberries.views import WildberriesView
from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.exceptions import ApplicationException
from app.infrastructure.services.parsers.product_marketplace.wildberries.request.keyword import (
    WildBerriesParserByNameRequest,
)
from app.infrastructure.utils.fetchers.aio_http import AiohttpFetcher

router = APIRouter(
    tags=['Wildberries parser handlers'],
    prefix="/wildberries"
)


@router.get(
    path="/products/{product_name}",
    status_code=status.HTTP_200_OK,
    description='Get all products from wildberries by name which user provide',
    responses={
        status.HTTP_200_OK: {'model': List[ProductMarketPlaceResponseSchema]},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    }
)
async def get_products_by_name(product_name: str) -> List[ProductMarketPlaceResponseSchema]:
    try:
        wildberries_view: WildberriesView = WildberriesView(parser=WildBerriesParserByNameRequest(AiohttpFetcher()))
        products: List[ProductMarketPlace] = await wildberries_view.get_products_by_name(name=product_name)
        return [ProductMarketPlaceResponseSchema.from_aggregate(pm) for pm in products]
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})


@router.get(
    path="/{article}",
    status_code=status.HTTP_200_OK,
    description='Get product by article from wildberries which user provide'
)
async def get_product_by_id(article: str):
    ...


@router.get(
    path="/{category_name}",
    status_code=status.HTTP_200_OK,
    description='Get all products from category wildberries which user provide'
)
async def get_products_by_category(category_name: str):
    ...


@router.get(
    path="/{brand_name}",
    status_code=status.HTTP_200_OK,
    description='Get all products from brand'
)
async def get_products_by_brand(brand_name: str):
    ...
