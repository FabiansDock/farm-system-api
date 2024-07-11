from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int): 
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_user

def get_user_by_email(db: Session, email: str): 
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_user

def get_users(db: Session):
    return db.query(models.User).filter().all()
    
def create_user(db: Session, user: any):
    user = jsonable_encoder(user)
    hashed_password = "hash" + user["password"]
    db_user = models.User(email=user["email"], hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user