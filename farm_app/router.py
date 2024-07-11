from typing import Annotated
from fastapi import APIRouter, Form, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/users", response_model=schemas.User, tags=["user"])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/user/email/{email}", response_model=schemas.User, tags=["user"])
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return crud.get_user_by_email(db, email)

@router.get("/user/{user_id}", response_model=schemas.User, tags=["user"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)    

@router.post("/user/", response_model=schemas.User, tags=["user"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
      
@router.post("/crop-disease/detect", response_model=schemas.CropDisease, tags=["crop-disease"])
def detect_crop_disease(image: Annotated[UploadFile, File()]):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")
    return {"disease": "ok", "confidence": "2.2", "recommendations": "ok"}