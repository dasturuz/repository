from pydantic import BaseModel
from pydantic.datetime_parse import datetime

from db import Base


class OrderBase(BaseModel):
    name: str
    date:datetime
    status: bool
    customer_id: int


class CreateBasket(OrderBase):
    pass


class UpdateBasket(OrderBase):
    id: int


class DeleteBasket(OrderBase):
    id:int