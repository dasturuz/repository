from db import Base
from sqlalchemy import String, Boolean, Integer, DateTime, func, Column, ForeignKey

class Expences(Base):
    __tablename__ = "Expences"
    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    type = Column(Integer(), ForeignKey("Product_types.id"), nullable=False)
    title = Column(String(30), nullable=False)
    worker_id = Column(Integer(), ForeignKey("Users.id"), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    user_id = Column(Integer(), ForeignKey("Users.id"), nullable=False)
    comment = Column(String(100), nullable=False)