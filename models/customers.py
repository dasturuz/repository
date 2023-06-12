from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column

class Customers(Base):
    __tablename__ = "Customers"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    phone = Column(String(20), nullable=False)
    adress = Column(String(50), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)