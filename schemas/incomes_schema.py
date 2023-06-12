from pydantic.datetime_parse import datetime
from db import Base
from pydantic import BaseModel

class IncomeBase(BaseModel):
    name: str
    price: int
    type:int
    title: str
    date:datetime
    comment:str
    status: bool


class CreateIncome(IncomeBase):
    date: datetime
    user_id:int
    order_id:int

class UpdateIncome(IncomeBase):
    id: int
    order_id: int
    user_id: int


class DeleteIncome(IncomeBase):
    id: int