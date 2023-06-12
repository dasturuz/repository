from pydantic.datetime_parse import datetime
from db import Base
from pydantic import BaseModel


class ExpenceBase(BaseModel):
    name: str
    type:int
    title: str
    date:datetime
    user_id:int
    comment:str


class CreateExpence(ExpenceBase):
    date: datetime
    worker_id: int
    status: bool


class UpdateExpence(ExpenceBase):
    id: int


class DeleteExpence(ExpenceBase):
    id: int