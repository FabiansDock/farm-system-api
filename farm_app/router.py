from fastapi import APIRouter
from .routers import users, cropDisease
from .database import Base, engine


Base.metadata.create_all(bind=engine)

router = APIRouter()

router.include_router(users.router)
router.include_router(cropDisease.router)
