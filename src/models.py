from sqlalchemy import Column, Integer, TIMESTAMP, Boolean, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

"""197325"""
class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    end_date = Column(TIMESTAMP, nullable=False)
    status = Column(String, nullable=False, default="not_sub")
    role = Column(Boolean, default=0)