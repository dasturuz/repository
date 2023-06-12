from pydantic import BaseModel
from pydantic.datetime_parse import datetime

from db import Base

class ProductBase(BaseModel):
    name: str
    old_price: int
    new_price: int
    type: int
    date:datetime
    status: bool

class CreateProduct(ProductBase):
    pass

class UpdateProduct(ProductBase):
    id: int

class DeleteProduct(ProductBase):
    id:int