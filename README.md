Esta api esta creada utilizando FastAPI, middleware, pydantic, Boostrap, Css, Javascrip
# Pasos para que funcione correctamente nuestra API

## 1. Descargar la carpeta comprimida:
Al descargar la carpeta, la debemos descomprimir. La cual contiene la API

## 2. Crear el entorno virtual:
```
python -m venv cafejardin
```
## 2. Activación  del entorno virtual:
```
cafejardin\Scripts\Activate
```
## 3. Instalación de librerias
```
pip install -r requirements.txt
```
## 4. Ejecución para obtener el endpoint
```
uvicorn main:app --reload
```
## 5. Configuración de la base de datos en MySQL:
   La conexión en la API y base de datos debe contar con el mismo usuario, contraseña y nombre de la base de datos asignados en MySQL
   en este caso.
   
![image](https://github.com/user-attachments/assets/0a6a5611-fdaf-4914-b651-6609787d4863)

