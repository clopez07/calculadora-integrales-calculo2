# 🧮 Calculadora de Integrales - Cálculo II

Una aplicación web educativa para calcular **integrales definidas**, diseñada específicamente para estudiantes de **Cálculo II**. Desarrollada con Python, Flask y SymPy para proporcionar cálculos precisos y visualizaciones interactivas.

## 🎯 Características Principales

- ✅ **Cálculo de área bajo la curva** - Integrales definidas con límites específicos
- ✅ **Cálculo de volumen de revolución** - Método del disco alrededor del eje X
- ✅ **Visualización gráfica interactiva** - Gráficos generados con Matplotlib
- ✅ **Editor matemático visual** - Botones para símbolos y funciones matemáticas
- ✅ **Explicación paso a paso** - Proceso educativo detallado del cálculo
- ✅ **Modal en pantalla completa** - Visualización ampliada de gráficos
- ✅ **Sintaxis matemática flexible** - Acepta múltiples formatos de entrada

## �️ Screenshots

### Interfaz Principal
*Próximamente - agrega screenshots de tu aplicación*

### Cálculo con Pasos Detallados
*Próximamente - agrega screenshots del proceso paso a paso*

## 🚀 Instalación y Ejecución

### **Requisitos Previos**
- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### **1. Clonar el repositorio**
```bash
git clone https://github.com/TU_USUARIO/calculadora-integrales.git
cd calculadora-integrales
```

### **2. Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
# o en Windows: venv\Scripts\activate
```

### **3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **4. Ejecutar la aplicación**

#### **Método 1: Script automático (Recomendado)**
```bash
./start.sh
```

#### **Método 2: Control interactivo**
```bash
./control.sh
```

#### **Método 3: Manual**
```bash
python app.py
```

### **5. Abrir en navegador**
Navega a: `http://127.0.0.1:8082`

## 📁 Estructura del proyecto

```
calculadora_integrales/
├── app.py              # 🖥️ Servidor Flask principal
├── start.sh            # 🚀 Script de inicio automático
├── stop.sh             # 🛑 Script de parada
├── control.sh          # 🎮 Control interactivo
├── templates/
│   └── index.html      # 🌐 Interfaz web Bootstrap + JavaScript
├── requirements.txt    # 📦 Dependencias del proyecto
├── .gitignore         # 🚫 Archivos excluidos de Git
└── README.md          # 📖 Este archivo
```

## 🎯 Ejemplos de uso

### **Funciones Polinómicas**
```
Función: 5*x**4 - 8*x**3 + 6
Límites: -1 a 4
Resultado: Área = 545 unidades cuadradas
```

### **Funciones Trigonométricas**
```
Función: sin(x)
Límites: 0 a pi
Resultado: Área = 2 unidades cuadradas
```

### **Funciones Exponenciales**
```
Función: exp(x)
Límites: 0 a 1
Resultado: Área ≈ 1.718 unidades cuadradas
```

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología | Propósito |
|------------|------------|-----------|
| **Backend** | Python + Flask | Servidor web y API REST |
| **Matemáticas** | SymPy | Cálculo simbólico y numérico |
| **Gráficos** | Matplotlib | Generación de visualizaciones |
| **Frontend** | Bootstrap 5 + JavaScript | Interfaz responsive |
| **Renderizado** | MathJax | Notación matemática LaTeX |
| **Entorno** | Virtual Environment | Aislamiento de dependencias |

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

Desarrollado para el curso de **Cálculo II** de la **Universidad Tecnológica de Honduras (UTH)**.

## 🙏 Agradecimientos

- SymPy community por la excelente librería de matemáticas simbólicas
- Flask team por el framework web minimalista
- Bootstrap team por el framework CSS
- MathJax por el renderizado de ecuaciones matemáticas
