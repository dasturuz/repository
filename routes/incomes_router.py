from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from pydantic.datetime_parse import date
from db import get_db
from functions.incomes_func import add_incomes, one_incomes, delete_incomes, update_incomes, all_incomes
from schemas.incomes_schema import *
import datetime

incomes_router = APIRouter()

@incomes_router.post("/add")
def incomes_qoshish(form:CreateIncome,db:Session=Depends(get_db)):
    return add_incomes(form=form,db=db)

@incomes_router.get("/read")
def get_incomes(search:str=None, status:bool=True, id: int=0, start_date:date=datetime.datetime.now().date().min, end_date: datetime.date =datetime.datetime.now().date().min, page:int=1, limit:int=2, db:Session=Depends(get_db)):
    if id:
        return one_incomes(id=id,db=db)
    else:
        return all_incomes(search=search, status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@incomes_router.put("/update")
def incomes_update(form:UpdateIncome,db:Session=Depends(get_db)):
   return update_incomes(form=form,db=db)

@incomes_router.delete("/delete")
def incomes_delete(id:int,db:Session=Depends(get_db)):
   return delete_incomes(id=id,db=db)