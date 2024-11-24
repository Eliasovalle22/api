from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.connection import get_db
from models.sqlalchemy_users import User as UserSQL
from models.sqlalchemy_products import Product as ProductSQL
from models.products import Product as ProductPydantic  # Modelo Pydantic
from models.users import User as UserPydantic  # Modelo Pydantic para validaciones
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()

# Crear un usuario
@app.post("/users")
async def create_user(user: UserPydantic, db: Session = Depends(get_db)):
    # Validar si el usuario ya existe
    db_user = db.query(UserSQL).filter(UserSQL.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    # Hashear la contraseña antes de guardarla
    hashed_password = pwd_context.hash(user.password)

    # Crear usuario con contraseña hasheada
    new_user = UserSQL(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "email": new_user.email}

# Obtener un usuario por ID
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id": user.id, "email": user.email}

# Listar usuarios
@app.get("/users")
async def list_users(db: Session = Depends(get_db)):
    users = db.query(UserSQL).all()
    return [{"id": user.id, "email": user.email} for user in users]

# Actualizar usuario
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserPydantic, db: Session = Depends(get_db)):
    db_user = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db_user.email = user.email

    # Hashear la nueva contraseña antes de guardarla
    db_user.password = pwd_context.hash(user.password)
    
    db.commit()
    return {"message": "Usuario actualizado correctamente"}

# Eliminar usuario
@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(db_user)
    db.commit()
    return {"message": "Usuario eliminado correctamente"}


# Crear producto
@app.post("/products")
async def create_product(product: ProductPydantic, db: Session = Depends(get_db)):
    new_product = ProductSQL(nombre=product.nombre, precio=product.precio)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"id": new_product.id, "nombre": new_product.nombre, "precio": new_product.precio}

# Listar productos
@app.get("/products")
async def list_products(db: Session = Depends(get_db)):
    products = db.query(ProductSQL).all()
    return [{"id": product.id, "nombre": product.nombre, "precio": product.precio} for product in products]

# Obtener producto por ID
@app.get("/products/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductSQL).filter(ProductSQL.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"id": product.id, "nombre": product.nombre, "precio": product.precio}

# Actualizar producto
@app.put("/products/{product_id}")
async def update_product(product_id: int, product: ProductPydantic, db: Session = Depends(get_db)):
    db_product = db.query(ProductSQL).filter(ProductSQL.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db_product.nombre = product.nombre
    db_product.precio = product.precio
    db.commit()
    return {"message": "Producto actualizado correctamente"}

# Eliminar producto
@app.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(ProductSQL).filter(ProductSQL.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(db_product)
    db.commit()
    return {"message": "Producto eliminado correctamente"}
        
        
# Verificar contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

@app.post('/login')
def login(user: UserPydantic, db: Session = Depends(get_db)):
    # Buscar usuario por correo electrónico
    db_user = db.query(UserSQL).filter(UserSQL.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Verificar la contraseña
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    return {"message": "Usuario autenticado correctamente"}
