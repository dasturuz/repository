from pydantic import BaseModel
from pydantic.datetime_parse import datetime

from db import Base


class CustomerBase(BaseModel):
    name: str
    phone: str
    adress: str
    date:datetime
    status:bool


class CreateCustomer(CustomerBase):
    date: datetime
    status: bool


class UpdateCustomer(CustomerBase):
    id: int


class DeleteCustomer(CustomerBase):
    id: int