from http.client import HTTPException

from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from pydantic.datetime_parse import date
from db import get_db
from functions.expences_func import add_expenses, one_expenses, delete_expenses, update_expenses, all_expenses
from routes.auth import get_current_active_user
from schemas.expences_schema import *
import datetime

from schemas.users import UserCurrent

expenses_router = APIRouter()

@expenses_router.post("/add")
def expenses_qoshish(form:CreateExpence,db:Session=Depends(get_db)):
    return add_expenses(form=form,db=db)

@expenses_router.get("/read")
def get_expenses(search:str=None, status:bool=True, id: int=0, start_date:date=datetime.datetime.now().date().min, end_date: datetime.date =datetime.datetime.now().date().min, page:int=1, limit:int=2, db:Session=Depends(get_db)):
    if id:
        return one_expenses(id=id,db=db)
    else:
        return all_expenses(search=search, status=status,start_date=start_date,end_date=end_date,page=page,limit=limit,db=db)


@expenses_router.put("/update")
def expenses_update(form:UpdateExpence,db:Session=Depends(get_db)):
   return update_expenses(form=form,db=db)

@expenses_router.delete("/delete")
def expenses_update(id:int,db:Session=Depends(get_db)):
   return delete_expenses(id=id,db=db)