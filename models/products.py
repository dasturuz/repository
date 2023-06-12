from pydantic import BaseModel
from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column, ForeignKey

class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    old_price = Column(Integer, nullable=False)
    new_price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    type = Column(String(30), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)