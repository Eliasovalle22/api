from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos MySQL
DATABASE_URL = "mysql+pymysql://root:1234@localhost/cafejardin"

# Crear motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Base para los modelos
Base = declarative_base()

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
