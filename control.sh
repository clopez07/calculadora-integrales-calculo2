#!/bin/bash

# 🎮 Control Center - Calculadora de Integrales
# Menú interactivo similar a MAMP

clear
echo "🧮===============================================🧮"
echo "       CALCULADORA DE INTEGRALES - Control      "
echo "             Cálculo II - UTH                    "
echo "🧮===============================================🧮"
echo ""
echo "Selecciona una opción:"
echo ""
echo "1) 🚀 Iniciar servidor"
echo "2) 🛑 Detener servidor"
echo "3) 🔄 Reiniciar servidor"
echo "4) 🌐 Abrir en navegador"
echo "5) 📊 Ver estado del servidor"
echo "6) 📋 Ver logs en tiempo real"
echo "7) ❌ Salir"
echo ""
read -p "Opción [1-7]: " opcion

case $opcion in
    1)
        echo "🚀 Iniciando servidor..."
        ./start.sh
        ;;
    2)
        echo "🛑 Deteniendo servidor..."
        ./stop.sh
        ;;
    3)
        echo "🔄 Reiniciando servidor..."
        ./stop.sh
        sleep 2
        ./start.sh
        ;;
    4)
        echo "🌐 Abriendo navegador..."
        if command -v open >/dev/null 2>&1; then
            open http://127.0.0.1:8082
        else
            echo "📋 Abre manualmente: http://127.0.0.1:8082"
        fi
        ;;
    5)
        echo "📊 Estado del servidor:"
        if lsof -ti:8082 > /dev/null 2>&1; then
            echo "✅ Servidor ACTIVO en puerto 8082"
            echo "🌐 URL: http://127.0.0.1:8082"
        else
            echo "❌ Servidor INACTIVO"
        fi
        ;;
    6)
        echo "📋 Logs en tiempo real (Ctrl+C para salir):"
        if ps aux | grep "[p]ython.*app.py" > /dev/null; then
            tail -f /dev/null # Placeholder - en producción usarías logs reales
        else
            echo "❌ Servidor no está ejecutándose"
        fi
        ;;
    7)
        echo "👋 ¡Hasta luego!"
        exit 0
        ;;
    *)
        echo "❌ Opción inválida"
        exit 1
        ;;
esac
