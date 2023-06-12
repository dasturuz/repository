from fastapi import Depends
from sqlalchemy.orm import Session
from models.customers import Customers
from db import Base, get_db
from schemas.users import *
from utils.pagination import pagination


def all_customers(search, status, roll, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Customers.name.like(search_formatted) | Customers.roll.like(search_formatted)
    else:
        search_filter = Customers.id > 0
    if status in [True, False]:
        status_filter = Customers.status == status
    else:
        status_filter = Customers.id > 0

    if roll:
        roll_filter = Customers.roll == roll
    else:
        roll_filter = Customers.id > 0

    products = db.query(Customers).filter(search_filter, status_filter, roll_filter).order_by(Customers.name.asc())
    if page and limit:
        return pagination(products, page, limit)
    else:
        return products.all()


def one_customer(id, db):
    return db.query(Customers).filter(Customers.id == id).first()


def customer_add(form, db):
    new_customer = Customers(
        name=form.name,
        phone=form.phone,
        adress=form.adress,
        date=form.date,
        status=form.status
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {"data": "Muvaffaqiyatli qo'shildi"}


def read_customer(db):
    users = db.query(Customers).all()
    return users


def update_customer(form, db):
    user = db.query(Customers).filter(Customers.id == form.id).update({
        Customers.id: form.id,
        Customers.name: form.name,
        Customers.date: form.date,
        Customers.phone: form.phone,
        Customers.status: form.status
    })
    db.commit()
    return {"Malumot yangilandi"}


def delete_customer(id: int, db):
    customer = db.query(Customers).filter(Customers.id == id).update({
        Customers.status: False
    })
    db.commit()
    return {"Malumot o'chirildi"}
