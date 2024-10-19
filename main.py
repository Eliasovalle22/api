from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from backend.connection import connection
from models.users import User
from models.products import Product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Listar usuarios
@app.get('/users')
async def get_users():
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT * FROM users'

    try:
        cursor.execute(query)
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los usuarios: {err}")
    finally:
        cursor.close()

# Listar usuarios por id
@app.get('/users/{user_id}')
async def get_user(user_id: int):
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT * FROM users WHERE id = %s'
    values = (user_id,)

    try:
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            return user
        else:
            raise HTTPException(
                status_code=404, detail=f"Usuario con id {user_id} no encontrado")
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener el usuario: {err}")
    finally:
        cursor.close()


# crear usuarios
@app.post('/users')
async def create_user(user: User):
    cursor = connection.cursor()
    query = 'INSERT INTO users (email, password) VALUES (%s, %s)'
    values = (user.email, user.password)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario creado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al crear el usuario: {err}")
    except ValueError as err:
        raise HTTPException(
            status_code=400, detail=f"Error en los valores: {err}")
    finally:
        cursor.close()


# Actualizar usuarios
@app.put('/users/{user_id}')
async def update_user(user_id: int, user: User):
    cursor = connection.cursor()
    query = 'UPDATE users SET email = %s, password = %s WHERE id = %s'
    values = (user.email, user.password, user_id)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail=f"Usuario con id {user_id} no encontrado")
        return {"message": "Usuario actualizado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar el usuario: {err}")
    except ValueError as err:
        raise HTTPException(
            status_code=400, detail=f"Error en los valores: {err}")
    finally:
        cursor.close()


#Eliminar usuarios
@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    cursor = connection.cursor()
    query = 'DELETE FROM users WHERE id = %s'
    values = (user_id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail=f"Usuario con id {user_id} no encontrado")
        return {"message": "Usuario eliminado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al eliminar el usuario: {err}")
    finally:
        cursor.close()


# Listar productos
@app.get('/products')
async def get_products():
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT * FROM products'

    try:
        cursor.execute(query)
        products = cursor.fetchall()
        return products
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los productos: {err}")
    finally:
        cursor.close()
        
# listar productos por id
@app.get('/products/{products_id}')
async def get_product(products_id: int):
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT * FROM products WHERE id = %s'
    values = (products_id,)

    try:
        cursor.execute(query, values)
        products = cursor.fetchone()
        if products:
            return products
        else:
            raise HTTPException(
                status_code=404, detail=f"producto con id {products_id} no encontrado")
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener el producto: {err}")
    finally:
        cursor.close()

# crear productos
@app.post('/products')
async def create_product(products: Product):
    cursor = connection.cursor()
    query = 'INSERT INTO products (nombre, precio) VALUES (%s, %s)'
    values = (products.nombre, products.precio)

    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Producto creado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al crear el Producto: {err}")
    except ValueError as err:
        raise HTTPException(
            status_code=400, detail=f"Error en los valores: {err}")
    finally:
        cursor.close()

# Actualizar productos
@app.put('/products/{products_id}')
async def update_product(products_id: int, products: Product):
    cursor = connection.cursor()
    query = 'UPDATE products SET nombre = %s, precio = %s WHERE id = %s'
    values = (products.nombre, products.precio, products_id)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail=f"producto con id {products_id} no encontrado")
        return {"message": "producto actualizado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar el producto: {err}")
    except ValueError as err:
        raise HTTPException(
            status_code=400, detail=f"Error en los valores: {err}")
    finally:
        cursor.close()

#Eliminar productos
@app.delete('/products/{products_id}')
async def delete_product(products_id: int):
    cursor = connection.cursor()
    query = 'DELETE FROM products WHERE id = %s'
    values = (products_id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail=f"producto con id {products_id} no encontrado")
        return {"message": "producto eliminado correctamente"}
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al eliminar el producto: {err}")
    finally:
        cursor.close()
        
        
#ingreso login
@app.post('/login')
def login(user: User):
    cursor = connection.cursor()
    query = 'SELECT * FROM users WHERE email = %s AND password = %s'
    values = (user.email, user.password)

    try:
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            return {"message": "Usuario autenticado correctamente"}
        else:
            raise HTTPException(
                status_code=404, detail="Usuario no encontrado contraseña incorrecta")
    except mysql.connector.Error as err:
        raise HTTPException(
            status_code=500, detail=f"Error al autenticar el usuario: {err}")
    finally:
        cursor.close()