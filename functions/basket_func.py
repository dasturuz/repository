from fastapi import Depends
from sqlalchemy.orm import Session
from models.basket import Basket
from db import Base, get_db
from schemas.users import *
from utils.pagination import pagination


def all_basket_products(search, status, roll, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Basket.name.like(search_formatted) | Basket.roll.like(search_formatted)
    else:
        search_filter = Basket.id > 0
    if status in [True, False]:
        status_filter = Basket.status == status
    else:
        status_filter = Basket.id > 0

    if roll:
        roll_filter = Basket.roll == roll
    else:
        roll_filter = Basket.id > 0

    basket = db.query(Basket).filter(search_filter, status_filter, roll_filter).order_by(Basket.name.asc())
    if page and limit:
        return pagination(basket, page, limit)
    else:
        return basket.all()


def one_basket_product(id, db):
    return db.query(Products).filter(Products.id == id).first()


def basket_add(form, db):
    new_basket_product = Basket(
        name=form.name,
        type=form.type,
        status=form.status
    )
    db.add(new_basket_product)
    db.commit()
    db.refresh(new_basket_product)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_product(db):
    users = db.query(Basket).all()
    return users


def update_basket(form, db):
    user = db.query(Basket).filter(Basket.id == form.id).update({
        Basket.id: form.id,
        Basket.name: form.name,
        Basket.date: form.date,
        Basket.status: form.status
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_Basket(id: int, db):
    product = db.query(Basket).filter(Basket.id == id).update({
        Basket.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
