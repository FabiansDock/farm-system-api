from sqlalchemy import Column, Integer, String, Float, LargeBinary, DateTime, ForeignKey, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class CropDisease(Base):
    __tablename__ = 'crop_diseases'

    id = Column(Integer, primary_key=True)
    image = Column(LargeBinary, nullable=False)
    disease = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    recommendations = Column(String, nullable=False)

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    precipitation = Column(Float, nullable=False)

class SoilHealth(Base):
    __tablename__ = 'soil_health'
    
    id = Column(Integer, primary_key=True)
    sensor_id = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    nutrient_levels = Column(JSON, nullable=False)  
    pH = Column(Float, nullable=False)
    moisture = Column(Float, nullable=False)

class VariableRateApplication(Base):
    __tablename__ = 'vra'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    crop_type = Column(String, nullable=False)
    current_conditions = Column(JSON, nullable=False)  
    fertilizer_application = Column(JSON, nullable=False)
    pesticide_application = Column(Float, nullable=False)
    water_application = Column(Float, nullable=False)

class Visualization(Base):
    __tablename__ = 'visualizations'

    id = Column(Integer, primary_key=True)
    farm_id = Column(String, nullable=False)
    maps = Column(LargeBinary, nullable=False)
    charts = Column(LargeBinary, nullable=False)
    graphs = Column(LargeBinary, nullable=False)