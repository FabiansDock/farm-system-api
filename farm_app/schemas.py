from typing import Literal, Annotated
from datetime import date, datetime
from pydantic import BaseModel, Field, Json, EmailStr, SecretStr
        
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: SecretStr


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class CropDisease(BaseModel):
    disease: str
    confidence: float
    recommendations: str

    class Config:
        from_attributes = True


class WeatherLocation(BaseModel):
    location: str


class WeatherForcast(BaseModel):
    date: Annotated[date, Field()]
    temperature: Annotated[float, Field(..., gt=-273.15, description="Temperature in degrees, must be above absolute zero")]
    unit: Literal['C', 'F']
    humidity: Annotated[float, Field(..., ge=0, le=100, description="Humidity percentage (0-100)")]
    precipitation: Annotated[float, Field(..., ge=0, description="Precipitation amount in mm")]

    class Config:
        from_attributes = True


class SoilHealth(BaseModel):
    id: int
    sensor_id: int
    timestamp: datetime
    nutrient_levels: Json
    pH: float
    moisture: float

    class Config:
        from_attributes = True