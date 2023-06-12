from fastapi import Depends
from sqlalchemy.orm import Session
from db import Base,get_db
from models.incomes import Incomes
from schemas.incomes_schema import *
from fastapi import HTTPException
import datetime

from utils.pagination import pagination


def add_incomes(form,db):
    new_income = Incomes(
        name = form.name,
        price = form.price,
        order_id = form.order_id,
        user_id = form.user_id,
        comment = form.comment,
        title = form.title,
        type = form.type,
        date = form.date,
        status = form.status
    )
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return {"data":"Ma'lumot Saqlandi"}

def all_incomes(search, status, start_date, end_date, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Incomes.price.like(search_formatted)|\
            Incomes.worker_id.like(search_formatted)|Incomes.user_id.like(search_formatted)
    else:
        search_filter = Incomes.id > 0
    if status in [True, False]:
        status_filter = Incomes.status == status
    else:
        status_filter = Incomes.status.in_([True, False])
    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date()+ datetime.timedelta(days=1)
    except Exception as error:
        raise HTTPException(status_code = 400, detail="Faqat yyy-mmm-dd formatda yozing ")
    dones = db.query(Incomes).filter(Incomes.date>start_date).filter(search_filter, status_filter).order_by(Incomes.id.desc())
    if page and limit:
        return pagination(dones, page, limit)
    else:
        return dones.all()


def one_incomes(id,db):
    incomes = db.query(Incomes).filter(Incomes.id==id).first()
    return incomes

def update_incomes(form,db):
    update_incomes = db.query(Incomes).filter(Incomes.id==form.id).update(
        {
            Incomes.id:form.id,
            Incomes.order_id:form.order_id,
            Incomes.user_id:form.user_id,
            Incomes.comment:form.comment,
            Incomes.status:form.status
        }
    )
    db.commit()
    return {"data": "Ma'lumot O'zgartirildi"}

def delete_incomes(id: int, db:Session=Depends(get_db)):
    odelete_incomes = db.query(Incomes).filter(Incomes.id==id).update(
        {
            Incomes.status:False
        }
    )
    db.commit()
    return {"data": "Ma'lumot O'chirildi"}