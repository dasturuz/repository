from fastapi import Depends
from sqlalchemy.orm import Session
from models.product_types import Product_types
from db import Base, get_db
from schemas.users import *
from utils.pagination import pagination


def all_products(search, status, roll, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Product_types.name.like(search_formatted)
    else:
        search_filter = Product_types.id > 0
    if status in [True, False]:
        status_filter = Product_types.status == status
    else:
        status_filter = Product_types.id > 0

    if roll:
        roll_filter = Product_types.roll == roll
    else:
        roll_filter = Product_types.id > 0

    product_types = db.query(Product_types).filter(search_filter, status_filter, roll_filter).order_by(Product_types.name.asc())
    if page and limit:
        return pagination(product_types, page, limit)
    else:
        return product_types.all()

def add_product_type(form, user, db):
    new_product = Product_types(
        name = form.name,
        date = form.date,
        status = form.status,
        user_id = user.id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"data":"Muvaffaqiyatli qo'shildi"}

def one_product_type(id, db):
	return db.query(Product_types).filter(Product_types.id == id).first()

def read_product_type(db):
    product_type = db.query(Product_types).all()
    return product_type

def update_product_type(form, db):
    user = db.query(Product_types).filter(Product_types.id == form.id).update({
        Product_types.id:form.id,
        Product_types.name:form.name,
        Product_types.date:form.date,
        Product_types.status:form.status
    })
    db.commit()
    return {"Malumot yangilandi"}

def delete_product_type(id:int, db):
    product_type = db.query(Product_types).filter(Product_types.id == id).update({
        Product_types.status:False
    })
    db.commit()
    return {"Malumot o'chirildi"}