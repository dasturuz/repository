from fastapi import Depends
from sqlalchemy.orm import Session
from db import Base,get_db
from models.expences import Expences
from schemas.expences_schema import *
from utils.pagination import pagination
from fastapi import HTTPException
import datetime


def add_expenses(form,db):
    new_expenses = Expences(
        worker_id = form.worker_id,
        user_id = form.user_id,
        type = form.type,
        name = form.name,
        title = form.title,
        date = form.date,
        comment = form.comment,
        status = form.status
    )
    db.add(new_expenses)
    db.commit()
    db.refresh(new_expenses)
    return {"data":"Ma'lumot Saqlandi"}

def all_expenses(search, status, start_date, end_date, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Expences.price.like(search_formatted)|\
            Expences.worker_id.like(search_formatted)|Expences.source.like(search_formatted)
    else:
        search_filter = Expences.id > 0
    if status in [True, False]:
        status_filter = Expences.status == status
    else:
        status_filter = Expences.status.in_([True, False])
    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date()+ datetime.timedelta(days=1)
    except Exception as error:
        raise HTTPException(status_code = 400, detail="Faqat yyy-mmm-dd formatda yozing ")
    dones = db.query(Expences).filter(Expences.date>start_date).filter(search_filter, status_filter).order_by(Expences.id.desc())
    if page and limit:
        return pagination(dones, page, limit)
    else:
        return dones.all()


def one_expenses(id,db):
    expenses = db.query(Expences).filter(Expences.id==id).first()
    return expenses

def update_expenses(form,db):
    update_expenses = db.query(Expences).filter(Expences.id==form.id).update(
        {
            Expences.id:form.id,
            Expences.user_id:form.user_id,
            Expences.comment:form.comment,
            Expences.worker_id:form.worker_id,
            Expences.price:form.price,
            Expences.status:form.status
        }
    )
    db.commit()
    return {"data": "Ma'lumot O'zgartirildi"}

def delete_expenses(id: int, db:Session=Depends(get_db)):
    odelete_expenses = db.query(Expences).filter(Expences.id==id).update(
        {
            Expences.status:False
        }
    )
    db.commit()
    return {"data": "Ma'lumot O'chirildi"}