from pydantic import BaseModel

from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column, ForeignKey

class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, nullable=False , primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)