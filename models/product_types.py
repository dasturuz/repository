from pydantic import BaseModel

from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column, ForeignKey

class Product_types(Base):
    __tablename__ = "Product_types"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    user_id = Column(Integer, nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)