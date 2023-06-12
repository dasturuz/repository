from fastapi import Depends
from sqlalchemy.orm import Session
from models.products import Products
from db import Base, get_db
from schemas.users import *
from utils.pagination import pagination


def all_products(search, status, roll, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Products.name.like(search_formatted) | Products.roll.like(search_formatted)
    else:
        search_filter = Products.id > 0
    if status in [True, False]:
        status_filter = Products.status == status
    else:
        status_filter = Products.id > 0

    if roll:
        roll_filter = Products.roll == roll
    else:
        roll_filter = Products.id > 0

    products = db.query(Products).filter(search_filter, status_filter, roll_filter).order_by(Products.name.asc())
    if page and limit:
        return pagination(products, page, limit)
    else:
        return products.all()


def one_product(id, db):
    return db.query(Products).filter(Products.id == id).first()


def product_add(form, user, db):
    new_product = Products(
        name=form.name,
        old_price=form.old_price,
        new_price=form.new_price,
        type=form.type,
        date=form.date,
        status=form.status,
        user_id = user.id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_product(db):
    users = db.query(Products).all()
    return users


def update_product(form, db):
    user = db.query(Products).filter(Products.id == form.id).update({
        Products.id: form.id,
        Products.name: form.name,
        Products.date: form.date,
        Products.new_price: form.new_price,
        Products.old_price: form.old_price,
        Products.status: form.status
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_product(id: int, db):
    product = db.query(Products).filter(Products.id == id).update({
        Products.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
