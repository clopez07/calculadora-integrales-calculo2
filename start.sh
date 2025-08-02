#!/bin/bash

# 🚀 Script de inicio automático para Calculadora de Integrales
# Similar a MAMP pero para Python + Flask

echo "🧮 Iniciando Calculadora de Integrales..."
echo "================================================"

# Verificar si estamos en el directorio correcto
if [ ! -f "app.py" ]; then
    echo "❌ Error: No se encuentra app.py"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "❌ Error: No se encuentra el entorno virtual 'venv'"
    echo "   Crea el entorno virtual primero con: python -m venv venv"
    exit 1
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Verificar que Flask esté instalado
if ! python -c "import flask" 2>/dev/null; then
    echo "❌ Error: Flask no está instalado en el entorno virtual"
    echo "   Instala las dependencias primero"
    exit 1
fi

# Matar cualquier proceso previo en el puerto
echo "🔍 Verificando puerto 8082..."
if lsof -ti:8082 > /dev/null 2>&1; then
    echo "⚠️  Puerto 8082 ocupado, liberando..."
    lsof -ti:8082 | xargs kill -9 2>/dev/null
    sleep 2
fi

# Ejecutar la aplicación
echo "🚀 Iniciando servidor Flask..."
echo "📊 URL: http://127.0.0.1:8082"
echo "🌐 ¡Abre tu navegador en esa dirección!"
echo "================================================"
echo "💡 Presiona Ctrl+C para detener el servidor"
echo ""

# Ejecutar app.py
python app.py
