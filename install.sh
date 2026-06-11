$FOLDER="<Carpeta contenedora del proyecto>"
py -m venv .vnen;
Set-Location $FOLDER; py -m venv .venv;
.\.venv\Scripts\pip install -r requirements.txt;
cd $FOLDER; 
.\.venv\Scripts\Activate.ps1;

# Para instalar más paquetes más adelante:
# pip install nombre-del-paquete
# pip freeze > requirements.txt   # guardar lo instalado
