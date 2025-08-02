#!/usr/bin/env python3
"""
Calculadora de Integrales - Aplicación Web
Flask + Bootstrap + Python para cálculos matemáticos
"""

from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt
import base64
import io
import json
from datetime import datetime
import os

# Configurar matplotlib para mejor renderizado
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

app = Flask(__name__)
CORS(app)

def parsear_numero(valor_str):
    """
    Convierte una cadena en un número o expresión simbólica.
    Maneja pi, e, fracciones y expresiones matemáticas.
    """
    if not valor_str or valor_str.strip() == '':
        return None, "Valor vacío"
    
    try:
        # Reemplazar algunos patrones comunes
        valor_str = valor_str.strip()
        valor_str = valor_str.replace('π', 'pi')
        valor_str = valor_str.replace('∞', 'oo')
        
        # Usar sympify para convertir la expresión
        resultado = sp.sympify(valor_str)
        return resultado, None
        
    except Exception as e:
        return None, f"Error al parsear '{valor_str}': {str(e)}"

class CalculadoraIntegrales:
    """Clase principal para calcular integrales y generar gráficos"""
    
    def __init__(self):
        """Inicializar la calculadora con la variable simbólica x"""
        self.x = sp.Symbol('x', real=True)
    
    def validar_funcion(self, func_str):
        """Validar y convertir la función a expresión simbólica"""
        try:
            if not func_str.strip():
                return None, "La función no puede estar vacía"
            
            # Reemplazar algunos patrones comunes para facilitar la entrada
            func_str = func_str.replace('^', '**')
            func_str = func_str.replace('π', 'pi')
            func_str = func_str.replace('sen', 'sin')
            func_str = func_str.replace('cos', 'cos')
            func_str = func_str.replace('tan', 'tan')
            func_str = func_str.replace('ln', 'log')
            func_str = func_str.replace('lg', 'log')
            
            # Convertir a expresión simbólica usando el símbolo x definido
            funcion = sp.sympify(func_str, locals={'x': self.x})
            
            # Verificar que la función contenga la variable x o sea una constante válida
            if not funcion.has(self.x):
                # Si es una constante numérica, convertirla a función de x
                if funcion.is_number:
                    funcion = funcion + 0*self.x  # Hacer que dependa de x
                else:
                    # Verificar si contiene otras variables diferentes a x
                    variables_libres = funcion.free_symbols
                    variables_no_x = [v for v in variables_libres if v != self.x]
                    if variables_no_x:
                        vars_str = ', '.join(str(v) for v in variables_no_x)
                        return None, f"La función contiene variables no reconocidas: {vars_str}. Use 'x' como variable."
                    else:
                        # Es una constante simbólica (como pi, e)
                        funcion = funcion + 0*self.x  # Hacer que dependa de x
            
            return funcion, None
            
        except Exception as e:
            return None, f"Error en la función: {str(e)}"
    
    def validar_limites(self, a_str, b_str):
        """Validar y convertir los límites de integración"""
        try:
            # Parsear límite inferior
            a, error_a = parsear_numero(a_str)
            if error_a:
                return None, None, f"Límite inferior: {error_a}"
            
            # Parsear límite superior
            b, error_b = parsear_numero(b_str)
            if error_b:
                return None, None, f"Límite superior: {error_b}"
            
            # Verificar que los límites sean válidos
            if a is None or b is None:
                return None, None, "Los límites no pueden estar vacíos"
            
            # Convertir a valores numéricos para comparación si es posible
            try:
                a_num = float(a.evalf())
                b_num = float(b.evalf())
                if a_num >= b_num:
                    return None, None, "El límite inferior debe ser menor que el superior"
            except:
                # Si no se pueden evaluar numéricamente, continuar
                pass
            
            return a, b, None
            
        except Exception as e:
            return None, None, f"Error en los límites: {str(e)}"
    
    def calcular_area(self, funcion, a, b, pasos=False):
        """Calcular el área bajo la curva"""
        try:
            # Calcular la integral definida
            integral_simbolica = sp.integrate(funcion, (self.x, a, b))
            
            # Evaluar numéricamente
            try:
                if integral_simbolica == 0:
                    integral_numerica = 0.0
                else:
                    integral_numerica = float(integral_simbolica.evalf())
            except:
                integral_numerica = "No se pudo evaluar numéricamente"
            
            if pasos:
                # Generar pasos detallados
                pasos_lista = []
                
                # Paso 1: Función original
                pasos_lista.append({
                    'descripcion': 'Función a integrar:',
                    'formula': f'f(x) = {sp.latex(funcion)}'
                })
                
                # Paso 2: Integral indefinida
                try:
                    antiderivada = sp.integrate(funcion, self.x)
                    pasos_lista.append({
                        'descripcion': 'Antiderivada (integral indefinida):',
                        'formula': f'\\int f(x) \\, dx = {sp.latex(antiderivada)} + C'
                    })
                except:
                    pasos_lista.append({
                        'descripcion': 'No se pudo calcular la antiderivada analíticamente',
                        'formula': ''
                    })
                
                # Paso 3: Integral definida
                pasos_lista.append({
                    'descripcion': 'Integral definida:',
                    'formula': f'\\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} {sp.latex(funcion)} \\, dx'
                })
                
                # Paso 4: Aplicar teorema fundamental del cálculo
                try:
                    antiderivada = sp.integrate(funcion, self.x)
                    valor_b = antiderivada.subs(self.x, b)
                    valor_a = antiderivada.subs(self.x, a)
                    
                    pasos_lista.append({
                        'descripcion': 'Aplicando el Teorema Fundamental del Cálculo:',
                        'formula': f'F({sp.latex(b)}) - F({sp.latex(a)}) = {sp.latex(valor_b)} - {sp.latex(valor_a)}'
                    })
                except:
                    pass
                
                # Paso 5: Resultado
                pasos_lista.append({
                    'descripcion': 'Resultado:',
                    'formula': f'= {sp.latex(integral_simbolica)}'
                })
                
                if isinstance(integral_numerica, (int, float)):
                    pasos_lista.append({
                        'descripcion': 'Valor numérico:',
                        'formula': f'\\approx {integral_numerica:.6f}'
                    })
                
                return integral_simbolica, integral_numerica, pasos_lista, None
            else:
                return integral_simbolica, integral_numerica, None
            
        except Exception as e:
            error_msg = f"Error al calcular el área: {str(e)}"
            if pasos:
                return None, None, [], error_msg
            else:
                return None, None, error_msg
    
    def calcular_volumen(self, funcion, a, b, pasos=False):
        """Calcular el volumen de revolución (método del disco)"""
        try:
            # Volumen = π * ∫[a,b] f(x)² dx
            funcion_cuadrado = funcion**2
            integral_simbolica = sp.pi * sp.integrate(funcion_cuadrado, (self.x, a, b))
            
            # Evaluar numéricamente
            try:
                if integral_simbolica == 0:
                    integral_numerica = 0.0
                else:
                    integral_numerica = float(integral_simbolica.evalf())
            except:
                integral_numerica = "No se pudo evaluar numéricamente"
            
            if pasos:
                # Generar pasos detallados
                pasos_lista = []
                
                # Paso 1: Función original
                pasos_lista.append({
                    'descripcion': 'Función a rotar alrededor del eje x:',
                    'formula': f'f(x) = {sp.latex(funcion)}'
                })
                
                # Paso 2: Fórmula del volumen
                pasos_lista.append({
                    'descripcion': 'Fórmula del volumen por revolución (método del disco):',
                    'formula': f'V = \\pi \\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} [f(x)]^2 \\, dx'
                })
                
                # Paso 3: Sustituir la función
                pasos_lista.append({
                    'descripcion': 'Sustituyendo f(x):',
                    'formula': f'V = \\pi \\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} [{sp.latex(funcion)}]^2 \\, dx'
                })
                
                # Paso 4: Expandir el cuadrado
                pasos_lista.append({
                    'descripcion': 'Expandiendo el cuadrado:',
                    'formula': f'V = \\pi \\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} {sp.latex(funcion_cuadrado)} \\, dx'
                })
                
                # Paso 5: Calcular la integral
                try:
                    integral_sin_pi = sp.integrate(funcion_cuadrado, (self.x, a, b))
                    pasos_lista.append({
                        'descripcion': 'Calculando la integral:',
                        'formula': f'\\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} {sp.latex(funcion_cuadrado)} \\, dx = {sp.latex(integral_sin_pi)}'
                    })
                except:
                    pass
                
                # Paso 6: Resultado final
                pasos_lista.append({
                    'descripcion': 'Volumen final:',
                    'formula': f'V = {sp.latex(integral_simbolica)}'
                })
                
                if isinstance(integral_numerica, (int, float)):
                    pasos_lista.append({
                        'descripcion': 'Valor numérico:',
                        'formula': f'V \\approx {integral_numerica:.6f} \\text{{ unidades cúbicas}}'
                    })
                
                return integral_simbolica, integral_numerica, pasos_lista, None
            else:
                return integral_simbolica, integral_numerica, None
            
        except Exception as e:
            error_msg = f"Error al calcular el volumen: {str(e)}"
            if pasos:
                return None, None, [], error_msg
            else:
                return None, None, error_msg
    
    def generar_grafico(self, funcion, a, b, mostrar_area=True):
        """Generar gráfico de la función con el área sombreada"""
        try:
            # Crear figura
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Convertir límites a valores numéricos
            a_num = float(a.evalf())
            b_num = float(b.evalf())
            
            # Crear rango de valores x más amplio para el contexto
            rango = b_num - a_num
            x_inicio = a_num - 0.5 * rango
            x_fin = b_num + 0.5 * rango
            
            # Generar puntos para la gráfica
            x_vals = np.linspace(x_inicio, x_fin, 1000)
            
            # Convertir la función simbólica a función numérica
            func_numerica = sp.lambdify(self.x, funcion, 'numpy')
            
            try:
                y_vals = func_numerica(x_vals)
            except:
                # Si hay problemas con la evaluación, usar un rango más pequeño
                x_vals = np.linspace(a_num, b_num, 100)
                y_vals = func_numerica(x_vals)
            
            # Graficar la función
            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'$f(x) = {sp.latex(funcion)}$')
            
            if mostrar_area:
                # Sombrear el área bajo la curva
                x_area = np.linspace(a_num, b_num, 100)
                y_area = func_numerica(x_area)
                ax.fill_between(x_area, 0, y_area, alpha=0.3, color='lightblue', 
                               label='Área bajo la curva')
            
            # Marcar los límites de integración
            ax.axvline(x=a_num, color='red', linestyle='--', alpha=0.7, label=f'$x = {sp.latex(a)}$')
            ax.axvline(x=b_num, color='red', linestyle='--', alpha=0.7, label=f'$x = {sp.latex(b)}$')
            
            # Configurar el gráfico
            ax.axhline(y=0, color='black', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(f'Gráfico de $f(x) = {sp.latex(funcion)}$', fontsize=14)
            ax.legend()
            
            # Ajustar los límites del gráfico
            y_min, y_max = ax.get_ylim()
            margen_y = (y_max - y_min) * 0.1
            ax.set_ylim(y_min - margen_y, y_max + margen_y)
            
            # Convertir a base64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
            buffer.seek(0)
            imagen_base64 = base64.b64encode(buffer.getvalue()).decode()
            plt.close(fig)
            
            return imagen_base64, None
            
        except Exception as e:
            return None, f"Error al generar el gráfico: {str(e)}"

# Crear instancia de la calculadora
calculadora = CalculadoraIntegrales()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    """Evitar error 404 del favicon"""
    return Response(status=204)

@app.route('/calcular', methods=['POST'])
def calcular():
    """Endpoint para realizar cálculos"""
    try:
        data = request.get_json()
        
        # Extraer datos
        func_str = data.get('funcion', '')
        a_str = data.get('limite_a', '')
        b_str = data.get('limite_b', '')
        calcular_area = data.get('calcular_area', False)
        calcular_volumen = data.get('calcular_volumen', False)
        mostrar_pasos_area = data.get('mostrar_pasos_area', False)
        mostrar_pasos_volumen = data.get('mostrar_pasos_volumen', False)
        
        # Validar función
        funcion, error = calculadora.validar_funcion(func_str)
        if error:
            return jsonify({'success': False, 'error': error})
        
        # Validar límites
        a, b, error = calculadora.validar_limites(a_str, b_str)
        if error:
            return jsonify({'success': False, 'error': error})
        
        # Verificar que al menos una opción esté seleccionada
        if not calcular_area and not calcular_volumen:
            return jsonify({'success': False, 'error': 'Selecciona al menos una opción de cálculo'})
        
        resultado = {
            'success': True,
            'funcion': str(funcion),
            'limite_a': str(a),
            'limite_b': str(b),
            'timestamp': datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        }
        
        # Calcular área si está seleccionado
        if calcular_area:
            if mostrar_pasos_area:
                area_sim, area_num, pasos_area, error = calculadora.calcular_area(funcion, a, b, pasos=True)
                if error:
                    return jsonify({'success': False, 'error': error})
                
                resultado['area'] = {
                    'simbolico': str(area_sim),
                    'numerico': area_num,
                    'pasos': pasos_area
                }
            else:
                area_sim, area_num, error = calculadora.calcular_area(funcion, a, b)
                if error:
                    return jsonify({'success': False, 'error': error})
                
                resultado['area'] = {
                    'simbolico': str(area_sim),
                    'numerico': area_num
                }
        
        # Calcular volumen si está seleccionado
        if calcular_volumen:
            if mostrar_pasos_volumen:
                vol_sim, vol_num, pasos_volumen, error = calculadora.calcular_volumen(funcion, a, b, pasos=True)
                if error:
                    return jsonify({'success': False, 'error': error})
                
                resultado['volumen'] = {
                    'simbolico': str(vol_sim),
                    'numerico': vol_num,
                    'pasos': pasos_volumen
                }
            else:
                vol_sim, vol_num, error = calculadora.calcular_volumen(funcion, a, b)
                if error:
                    return jsonify({'success': False, 'error': error})
                
                resultado['volumen'] = {
                    'simbolico': str(vol_sim),
                    'numerico': vol_num
                }
        
        # Generar gráfico
        imagen_base64, error = calculadora.generar_grafico(funcion, a, b, calcular_area)
        if error:
            return jsonify({'success': False, 'error': error})
        
        resultado['grafico'] = imagen_base64
        
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error inesperado: {str(e)}'})

@app.route('/ejemplo/<nombre>')
def ejemplo(nombre):
    """Endpoint para cargar ejemplos predefinidos"""
    ejemplos = {
        'parabola': {
            'funcion': 'x**2',
            'limite_a': '0',
            'limite_b': '2',
            'calcular_area': True,
            'calcular_volumen': False
        },
        'seno': {
            'funcion': 'sin(x)',
            'limite_a': '0',
            'limite_b': 'pi',
            'calcular_area': True,
            'calcular_volumen': False
        },
        'exponencial': {
            'funcion': 'exp(x)',
            'limite_a': '0',
            'limite_b': '1',
            'calcular_area': True,
            'calcular_volumen': False
        },
        'cubica': {
            'funcion': 'x**3',
            'limite_a': '-1',
            'limite_b': '1',
            'calcular_area': True,
            'calcular_volumen': True
        }
    }
    
    if nombre in ejemplos:
        return jsonify({'success': True, 'ejemplo': ejemplos[nombre]})
    else:
        return jsonify({'success': False, 'error': 'Ejemplo no encontrado'})

if __name__ == '__main__':
    print("🚀 Iniciando Calculadora de Integrales Web...")
    print("📊 Servidor Flask corriendo en: http://127.0.0.1:8082")
    print("🌐 Abre tu navegador en esa dirección")
    app.run(debug=True, host='127.0.0.1', port=8082)
