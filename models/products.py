from pydantic import BaseModel, Field

class Product(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    precio: float = Field(..., gt=0)  # Cambiar Decimal por float
