from db import SessionLocal
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session

from models.users import Users
from routes import users,auth,product_router, customer_router, basket_router, orders_router, expences_router, incomes_router
from db import Base, engine
import datetime
from routes import product_type_router
from routes.auth import get_password_hash

Base.metadata.create_all(bind=engine)


app=FastAPI(
	title="SeniorDev",
)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get('/')
def home():
	return {"message": "Welcome"}
app.include_router(
	auth.login_router,
	prefix='/auth',
	tags=['User auth section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	users.router_user,
	prefix='/user',
	tags=['User section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	product_router.product_router,
	prefix='/products',
	tags=['Products section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	product_type_router.product_type_router,
	prefix='/product_types',
	tags=['Product Types section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	customer_router.router_cutomer,
	prefix='/customers',
	tags=['Customers section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	basket_router.router_basket,
	prefix='/basket',
	tags=['Basket Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	orders_router.router_order,
	prefix='/orders',
	tags=['Orders Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	expences_router.expenses_router,
	prefix='/expences',
	tags=['Expences Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

app.include_router(
	incomes_router.incomes_router,
	prefix='/incomes',
	tags=['Incomes Section'],
	responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
	           401: {'desription': 'Unauthorized'}}
)

try:
	db=SessionLocal()
	new_user_db = Users(
		name='www',
		username='www',
		number='form.number',
		password=get_password_hash('111111'),
		roll='www',
		status=True,

	)
	db.add(new_user_db)
	db.commit()
	db.refresh(new_user_db)
except Exception :
	print(Exception)