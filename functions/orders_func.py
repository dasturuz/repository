from fastapi import Depends
from sqlalchemy.orm import Session
from models.orders import Orders
from db import Base, get_db
from schemas.users import *
from utils.pagination import pagination


def all_orders(search, status, roll, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Orders.name.like(search_formatted) | Orders.roll.like(search_formatted)
    else:
        search_filter = Orders.id > 0
    if status in [True, False]:
        status_filter = Orders.status == status
    else:
        status_filter = Orders.id > 0

    if roll:
        roll_filter = Orders.roll == roll
    else:
        roll_filter = Orders.id > 0

    basket = db.query(Orders).filter(search_filter, status_filter, roll_filter).order_by(Orders.customer_id.asc())
    if page and limit:
        return pagination(basket, page, limit)
    else:
        return basket.all()


def one_order(id, db):
    return db.query(Orders).filter(Orders.id == id).first()


def order_add(form, db):
    new_order = Orders(
        status=form.status,
        customer_id =form.customer_id
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_order(db):
    users = db.query(Orders).all()
    return users


def update_order(form, db):
    user = db.query(Orders).filter(Orders.id == form.id).update({
        Orders.id: form.id,
        Orders.customer_id: form.customer_id,
        Orders.date: form.date,
        Orders.status: form.status
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_order(id: int, db):
    order = db.query(Orders).filter(Orders.id == id).update({
        Orders.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
