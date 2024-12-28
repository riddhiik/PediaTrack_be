from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

class pediatric_growth(BaseModel):
    height: float
    weight: float