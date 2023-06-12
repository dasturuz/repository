from pydantic import BaseModel
from pydantic.datetime_parse import datetime

from db import Base


class BasketBase(BaseModel):
    name: str
    type: int
    date:datetime
    status: bool


class CreateBasket(BasketBase):
    pass


class UpdateBasket(BasketBase):
    id: int


class DeleteBasket(BasketBase):
    id:int