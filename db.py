from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

from schemas import pediatric_growth

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Gaurav@localhost/pediatric_growth"

pool_size = 100
max_overflow = 35

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=pool_size, max_overflow=max_overflow
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Dependency
def get_db():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
    except Exception as e:
        db.close()
        print("Database error", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database Error! Please try again later",
        )

    try:
        yield db
    finally:
        db.close()
