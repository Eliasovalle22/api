from pydantic import BaseModel, Field, condecimal
from decimal import Decimal

class Product(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    precio: Decimal = condecimal(gt=0, decimal_places=2)