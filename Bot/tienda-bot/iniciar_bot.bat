@echo off
REM Script para iniciar TechStore Bot en Windows

echo.
echo ====================================
echo   TechStore Bot - Iniciando...
echo ====================================
echo.

REM Verificar si existe el entorno virtual
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Instalar/actualizar dependencias
echo Instalando dependencias...
pip install -r requirements.txt

REM Iniciar la aplicación
echo.
echo ====================================
echo   Bot iniciado en http://localhost:5000
echo ====================================
echo.
python app.py

pause
