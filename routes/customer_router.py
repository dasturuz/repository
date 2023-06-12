
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)


from functions.customers_func import one_customer, all_customers, update_customer, customer_add, delete_customer
from schemas.customers_schema import CreateCustomer,UpdateCustomer,CustomerBase,DeleteCustomer

router_cutomer = APIRouter()



@router_cutomer.post('/add',)
def add_customer(form: CreateCustomer, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : #
    if customer_add(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")


@router_cutomer.get('/',  status_code = 200)
def get_users(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_customer(id, db)
    else :
        return all_customers(search, status,roll, page, limit, db)


@router_cutomer.put("/update")
def user_update(form: UpdateCustomer, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)) :
    if update_customer(form, db) :
        raise HTTPException(status_code = 200, detail = "Amaliyot muvaffaqiyatli amalga oshirildi")




@router_cutomer.delete('/{id}',  status_code = 200)
def cutomer_delete(id: int = 0,db: Session = Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)) : # current_user: User = Depends(get_current_active_user)
    if id :
        return delete_customer(id, db)