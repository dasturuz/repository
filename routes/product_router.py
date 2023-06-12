from fastapi import APIRouter
from functions.product_func import *
from routes.auth import get_current_active_user
from schemas.products_schema import *

product_router = APIRouter()

@product_router.post("/add")
def add_product(form:CreateProduct, db:Session=Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return product_add(form=form, db=db, user=current_user)

@product_router.get('/',  status_code = 200)
def get_products(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_product(id, db)
    else :
        return all_products(search, status,roll, page, limit, db)

@product_router.put("/update")
def product_update(form:UpdateProduct, db:Session=Depends(get_db)):
    return update_product(form=form, db=db)

@product_router.delete("/delete")
def product_delete(id:int, db:Session=Depends(get_db)):
    return delete_product(id=id, db=db)