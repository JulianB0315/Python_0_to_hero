#!/bin/bash

# Script para iniciar TechStore Bot en macOS/Linux

echo ""
echo "===================================="
echo "   TechStore Bot - Iniciando..."
echo "===================================="
echo ""

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar/actualizar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Iniciar la aplicación
echo ""
echo "===================================="
echo "   Bot iniciado en http://localhost:5000"
echo "===================================="
echo ""
python3 app.py
