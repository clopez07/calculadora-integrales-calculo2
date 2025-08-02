#!/bin/bash

# 🛑 Script para detener la Calculadora de Integrales
# Similar al "Stop" de MAMP

echo "🛑 Deteniendo Calculadora de Integrales..."
echo "================================================"

# Buscar y matar procesos de Flask
PIDS=$(ps aux | grep "[p]ython.*app.py" | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo "ℹ️  No hay procesos de la calculadora ejecutándose"
else
    echo "🔍 Encontrados procesos: $PIDS"
    echo "$PIDS" | xargs kill -TERM 2>/dev/null
    sleep 2
    
    # Verificar si aún están corriendo y forzar cierre
    REMAINING=$(ps aux | grep "[p]ython.*app.py" | awk '{print $2}')
    if [ ! -z "$REMAINING" ]; then
        echo "⚡ Forzando cierre de procesos restantes..."
        echo "$REMAINING" | xargs kill -9 2>/dev/null
    fi
fi

# Liberar puerto 8082
if lsof -ti:8082 > /dev/null 2>&1; then
    echo "🔓 Liberando puerto 8082..."
    lsof -ti:8082 | xargs kill -9 2>/dev/null
fi

echo "✅ Calculadora de Integrales detenida correctamente"
echo "================================================"
