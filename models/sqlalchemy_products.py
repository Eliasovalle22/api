from sqlalchemy import Column, Integer, String, Float
from backend.connection import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
