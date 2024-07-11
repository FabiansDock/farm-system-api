from fastapi import APIRouter
from .database import SessionLocal


router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

