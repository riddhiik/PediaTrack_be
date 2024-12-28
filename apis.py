from re import compile
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import Optional, Literal
import re
from db import get_db


route = APIRouter(prefix="", tags=["Basic"])


@route.get("/greet")
def welcome():
    response = "Hello Riddhi! Please contact me for more information"
    
    return response
    
