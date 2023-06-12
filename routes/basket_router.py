
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from functions.basket_func import *
from schemas.basket_schema import *

router_basket = APIRouter()



@router_basket.post('/add',)
def add_customer(form: CreateBasket, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) :
    if basket_add(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")


@router_basket.get('/',  status_code = 200)
def get_basket_products(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_basket_product(id, db)
    else :
        return all_basket_products(search, status,roll, page, limit, db)


@router_basket.put("/update")
def user_update(form: UpdateBasket, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)) :
    if update_basket(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")




@router_basket.delete('/{id}',  status_code = 200)
def basket_delete(id: int = 0,db: Session = Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)) : # current_user: User = Depends(get_current_active_user)
    if id :
        return basket_delete(id, db)