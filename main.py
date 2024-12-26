from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Gaurav@localhost/pediatric_growth"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# used for data validation 
class pediatric_growth(BaseModel):
    height: float
    weight: float
#SQLalchemy models
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

#FastApi App
app = FastAPI()
async def add_growth_data(data:pediatric_growth):
    # Example logic to save growth data (you'll need to connect to the DB)
    return {"message": "Growth data added successfully"}