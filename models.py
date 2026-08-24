# models.py
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from config import engine

Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float)
    humidity = Column(Float)
    location = Column(String)


Base.metadata.create_all(engine)