from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la URL de conexión
DATABASE_URL = "mysql+pymysql://root:1234@localhost/cafejardin"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear el constructor de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir los modelos
Base = declarative_base()

# Dependencia para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
