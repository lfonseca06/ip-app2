# ip-app

## Para validar en el entorno de desarrollo
fastapi dev src/main.py

## Ver bases de datos en el archivo local
sqlite3 db.sqlite3  
.tables  
.schema transaction  

## Si reconstruyo el codespaces se me pierde la instalación de Azure cli y toca volverlo a instalar con:
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

## Creando el espacio vitual
python -m venv venv

## Para activar el entorno en linux
source venv/bin/activate

## Recargar en un puerto
uvicorn main:app --reload

## Saber cuál es el interprete (venv) utilizado
which python

## agregar el path del interprete
Ctrl + Shif + P  
Python: Select interpreter  
pegar ruta que sale del comando which python  

## Realizar pruebas en el código
pytest test_customers.py -v