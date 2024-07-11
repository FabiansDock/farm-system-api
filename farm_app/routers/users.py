from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database


router = APIRouter(tags=["user"])


def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/users", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.get("/user/email/{email}", response_model=schemas.User)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return crud.get_user_by_email(db, email)


@router.get("/user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@router.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
