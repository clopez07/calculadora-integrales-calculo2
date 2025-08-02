# 🧮 Calculadora de Integrales - UTH Cálculo II

**Universidad Tecnológica de Honduras (UTH)**  
**Ingeniería en Computación • Cálculo II**

Una aplicación web educativa avanzada para el cálculo de **integrales definidas**, diseñada específicamente para estudiantes de **Cálculo II**. Desarrollada con Python, Flask y SymPy para proporcionar cálculos matemáticos precisos, visualizaciones interactivas y explicaciones paso a paso.

## ✨ Características Principales

### 🧮 Cálculos Matemáticos
- ✅ **Área bajo la curva** - Integrales definidas ∫[a→b] f(x)dx
- ✅ **Volumen de revolución** - Método del disco π∫[a→b] [f(x)]²dx
- ✅ **Cálculo simbólico y numérico** - Resultados exactos y aproximados
- ✅ **Explicación paso a paso** - Proceso educativo detallado

### 🎨 Interfaz de Usuario
- ✅ **Editor matemático visual** - Botones para símbolos y funciones
- ✅ **Diseño responsive** - Compatible con dispositivos móviles
- ✅ **Branding universitario** - Logos UTH e Ingeniería en Computación
- ✅ **Interfaz moderna** - Bootstrap 5 con gradientes y animaciones

### 📊 Visualización
- ✅ **Gráficos interactivos** - Generados con Matplotlib
- ✅ **Modal en pantalla completa** - Visualización ampliada
- ✅ **Renderizado LaTeX** - Ecuaciones matemáticas con MathJax
- ✅ **Área sombreada** - Visualización clara del área calculada

### 🔧 Funcionalidades Técnicas
- ✅ **Sintaxis flexible** - Múltiples formatos de entrada
- ✅ **Validación de entrada** - Manejo robusto de errores
- ✅ **Ejemplos predefinidos** - Parábola, seno, exponencial, cúbica
- ✅ **Loading states** - Indicadores de progreso

## 🎯 Funciones Matemáticas Soportadas

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| **Polinómicas** | `x**n` | `x**2`, `3*x**3 + 2*x - 1` |
| **Trigonométricas** | `sin(x)`, `cos(x)`, `tan(x)` | `sin(x)`, `2*cos(x)` |
| **Exponenciales** | `exp(x)` | `exp(x)`, `2*exp(-x)` |
| **Logarítmicas** | `log(x)` | `log(x)`, `log(x+1)` |
| **Raíces** | `sqrt(x)` | `sqrt(x)`, `sqrt(x**2 + 1)` |
| **Constantes** | `pi`, `e` | `pi*x`, `e**x` |

## 🚀 Instalación y Ejecución

### **Requisitos Previos**
- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### **1. Clonar el repositorio**
```bash
git clone https://github.com/clopez07/calculadora-integrales-calculo2.git
cd calculadora-integrales-calculo2
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
chmod +x start.sh
./start.sh
```

#### **Método 2: Control interactivo**
```bash
chmod +x control.sh
./control.sh
```

#### **Método 3: Manual**
```bash
python main.py
```

### **5. Abrir en navegador**
Navega a: `http://127.0.0.1:5000`

## 📁 Estructura del Proyecto

```
calculadora_integrales/
├── 📄 main.py              # 🖥️ Servidor Flask principal
├── 📄 gui.py               # 🎨 Interfaz gráfica alternativa
├── 🚀 start.sh             # 🚀 Script de inicio automático
├── 🛑 stop.sh              # 🛑 Script de parada
├── 🎮 control.sh           # 🎮 Control interactivo
├── 📁 templates/
│   └── 🌐 index.html       # 🌐 Interfaz web principal
├── 📁 static/
│   └── 📁 images/          # 🖼️ Logos UTH e Ingeniería
│       ├── UTH.png
│       └── IC.png
├── 📦 requirements.txt     # 📦 Dependencias del proyecto
├── 🚫 .gitignore          # 🚫 Archivos excluidos de Git
└── 📖 README.md           # 📖 Este archivo
```

## 💡 Ejemplos de Uso

### **1. Función Polinómica**
```
Función: x**2
Límites: 0 a 2
Área: 8/3 ≈ 2.6667 unidades²
Volumen: 32π/5 ≈ 20.1062 unidades³
```

### **2. Función Trigonométrica**
```
Función: sin(x)
Límites: 0 a pi
Área: 2 unidades²
Volumen: π²/2 ≈ 4.9348 unidades³
```

### **3. Función Exponencial**
```
Función: exp(x)
Límites: 0 a 1
Área: e - 1 ≈ 1.7183 unidades²
Volumen: π(e² - 1)/2 ≈ 17.7711 unidades³
```

### **4. Función Compleja**
```
Función: x**3 - 2*x**2 + x + 1
Límites: -1 a 2
Área: 9/4 = 2.25 unidades²
Volumen: 243π/70 ≈ 10.9477 unidades³
```

## 🛠️ Tecnologías Utilizadas

### **Backend**
- **Python 3.9+** - Lenguaje de programación principal
- **Flask 2.3.3** - Framework web minimalista
- **SymPy 1.12** - Biblioteca de matemáticas simbólicas
- **Matplotlib 3.7.2** - Generación de gráficos
- **NumPy 1.25.2** - Cálculos numéricos

### **Frontend**
- **HTML5** - Estructura semántica
- **Bootstrap 5.3.0** - Framework CSS responsive
- **JavaScript ES6+** - Interactividad y API calls
- **MathJax 3** - Renderizado de ecuaciones LaTeX
- **Bootstrap Icons** - Iconografía moderna

### **Herramientas**
- **Git** - Control de versiones
- **GitHub** - Repositorio remoto
- **Virtual Environment** - Aislamiento de dependencias

## 🎓 Aspectos Educativos

### **Conceptos de Cálculo II Cubiertos**
- ✅ Integrales definidas
- ✅ Teorema fundamental del cálculo
- ✅ Área bajo curvas
- ✅ Volúmenes de revolución
- ✅ Método del disco
- ✅ Aplicaciones de integrales

### **Ventajas Pedagógicas**
- 📚 **Visualización clara** - Gráficos que facilitan comprensión
- 🔍 **Proceso paso a paso** - Explicación detallada de cálculos
- ⚡ **Verificación instantánea** - Comprobación rápida de resultados
- 🎯 **Ejemplos diversos** - Variedad de tipos de funciones
- 📱 **Accesibilidad** - Disponible en cualquier dispositivo

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Fork** el repositorio
2. Crea una **rama feature** (`git checkout -b feature/NuevaCaracteristica`)
3. **Commit** tus cambios (`git commit -m 'Agregar nueva característica'`)
4. **Push** a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un **Pull Request**

### **Ideas para Contribuir**
- 🔧 Nuevos tipos de integrales (impropias, múltiples)
- 📊 Más métodos de visualización
- 🌐 Soporte para más idiomas
- 📱 Aplicación móvil nativa
- 🧮 Más ejemplos educativos

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Información del Proyecto

**Desarrollado para:**
- **Universidad:** Universidad Tecnológica de Honduras (UTH)
- **Carrera:** Ingeniería en Computación
- **Curso:** Cálculo II
- **Período:** II Período 2025

**Repositorio:** https://github.com/clopez07/calculadora-integrales-calculo2

## 🙏 Agradecimientos

- **SymPy Community** - Excelente biblioteca de matemáticas simbólicas
- **Flask Team** - Framework web elegante y minimalista
- **Bootstrap Team** - Framework CSS responsive
- **MathJax** - Renderizado perfecto de ecuaciones matemáticas
- **Universidad Tecnológica de Honduras** - Apoyo educativo
- **Profesores de Cálculo II** - Inspiración y orientación académica

---

**📧 Contacto:** [GitHub Issues](https://github.com/clopez07/calculadora-integrales-calculo2/issues)  
**🌟 ¡No olvides dar una estrella al proyecto si te resultó útil!**
