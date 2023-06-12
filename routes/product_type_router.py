from fastapi import APIRouter
from functions.product_type_func import *
from routes.auth import get_current_active_user
from schemas.product_type_schema import *

product_type_router = APIRouter()

@product_type_router.post("/add")
def type_plus(form:CreateProductType, db:Session=Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)):
    return add_product_type(form=form, db=db, user=current_user)

@product_type_router.get('/',  status_code = 200)
def get_product_types(search: str = None, status: bool = True, id: int = 0,roll : str = None, page: int = 1, limit: int = 25, db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user) ) : # current_user: User = Depends(get_current_active_user)
    if id :
        return one_product_type(id, db)
    else :
        return all_products(search, status,roll, page, limit, db)

@product_type_router.put("/update")
def product_type_update(form:UpdateProductType, db:Session=Depends(get_db)):
    return update_product_type(form=form, db=db)

@product_type_router.delete("/delete")
def product_type_delete(id:int, db:Session=Depends(get_db)):
    return delete_product_type(id=id, db=db)