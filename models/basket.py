from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column, ForeignKey
from .product_types import Product_types
class Basket(Base):
    __tablename__ = "Basket"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    type = Column(Integer, ForeignKey(Product_types.id), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)