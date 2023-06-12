from pydantic import BaseModel
from pydantic.datetime_parse import datetime

from db import Base


class ProductTypeBase(BaseModel):
    name: str
    date:datetime
    status: bool


class CreateProductType(ProductTypeBase):
    pass


class UpdateProductType(ProductTypeBase):
    id: int


class DeleteProductType(ProductTypeBase):
    id:int