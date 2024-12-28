
from sqlalchemy import  Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import  declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String)

class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    birth_date = Column(Date)
    gender = Column(String(10))

class GrowthDataModel(Base):
    __tablename__ = "growth_data"
    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer, ForeignKey("children.id"))
    height = Column(Float)
    weight = Column(Float)
    recorded_at = Column(TIMESTAMP)
