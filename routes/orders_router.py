
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from functions.orders_func import *
from schemas.orders import *

router_order = APIRouter()



@router_order.post('/add',)
def add_order(form: CreateBasket, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : #
    if order_add(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")


@router_order.get('/',  status_code = 200)
def get_orders(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_order(id, db)
    else :
        return all_orders(search, status,roll, page, limit, db)


@router_order.put("/update")
def order_update(form: UpdateBasket, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)) :
    if update_order(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")




@router_order.delete('/{id}',  status_code = 200)
def order_delete(id: int = 0,db: Session = Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)) : # current_user: User = Depends(get_current_active_user)
    if id :
        return order_delete(id, db)