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

## Crear la App Service (Comando principal)
az webapp up --name $NOMBRE_APP --runtime "PYTHON:3.12" --resource-group "${NOMBRE_APP}-rg" --location canadacentral --sku F1 --logs

## Configurar el comando de Inicio
az webapp config set --name $NOMBRE_APP --resource-group "${NOMBRE_APP}-rg" --startup-file "startup.sh"

## Activar instalación automática de Dependencias (Paso crítico para que funcione)
az webapp config appsettings set --name $NOMBRE_APP --resource-group "${NOMBRE_APP}-rg" --settings SCM_DO_BUILD_DURING_DEPLOYMENT=True

## Verificar la configuración
az webapp config appsettings list --name $NOMBRE_APP --resource-group "${NOMBRE_APP}-rg" --query "[?name=='SCM_DO_BUILD_DURING_DEPLOYMENT']"

## 6. Empaquetar y subir el código
zip -r deploy.zip . -x "*.git*" "*__pycache__*" "*.venv*" "*.idea*" "*.vscode*"

## Subir a Azure
az webapp deployment source config-zip --name $NOMBRE_APP --resource-group "${NOMBRE_APP}-rg" --src deploy.zip  
rm deploy.zip

## Ver el proceso del despliegue
az webapp log tail --name $NOMBRE_APP --resource-group "${NOMBRE_APP}-rg"
