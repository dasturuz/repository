from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column, ForeignKey

class Incomes(Base):
    __tablename__ = "Incomes"
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)
    type = Column(String(50), ForeignKey("Product_types.name"), nullable=False)
    title = Column(String(60), nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("Orders.id"), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    comment = Column(String(100), nullable=False)
    status=  Column(Boolean, nullable=False, default=True)