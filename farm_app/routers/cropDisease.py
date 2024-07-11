from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .. import schemas

router = APIRouter(prefix="/crop-disease", tags=["crop-disease"])


@router.post("/detect", response_model=schemas.CropDisease)
def detect_crop_disease(image: Annotated[UploadFile, File()]):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")
    return {"disease": "ok", "confidence": "2.2", "recommendations": "ok"}
