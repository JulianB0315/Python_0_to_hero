from flask import Flask, request, jsonify, render_template, session
import json
import re
from datetime import datetime
import os
from functools import wraps
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_2024'

# Cargar productos
def cargar_productos():
    # Obtener la ruta del directorio actual del archivo app.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    productos_path = os.path.join(base_dir, 'productos.json')
    with open(productos_path, 'r', encoding='utf-8') as f:
        return json.load(f)['productos']

PRODUCTOS = cargar_productos()

# Cargar respuestas fluidas desde JSON
def cargar_respuestas_fluidas():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    respuestas_path = os.path.join(base_dir, 'respuestas_fluidas.json')
    with open(respuestas_path, 'r', encoding='utf-8') as f:
        return json.load(f)

RESPUESTA_FLUIDAS = cargar_respuestas_fluidas()

# Función para obtener respuesta aleatoria por intención
def obtener_respuesta(intencion, fecha_actual=None):
    """Obtiene una respuesta aleatoria según la intención"""
    respuestas_db = RESPUESTA_FLUIDAS['respuestas']
    
    if intencion in respuestas_db:
        respuestas_list = respuestas_db[intencion]['respuestas']
        respuesta = random.choice(respuestas_list)
        
        # Reemplazar placeholders de fecha/hora si es necesario
        if '{hora}' in respuesta or '{dia}' in respuesta:
            if fecha_actual is None:
                fecha_actual = datetime.now()
            
            respuesta = respuesta.replace('{hora}', fecha_actual.strftime('%H:%M'))
            respuesta = respuesta.replace('{dia}', fecha_actual.strftime('%d'))
            respuesta = respuesta.replace('{mes}', fecha_actual.strftime('%B'))
            respuesta = respuesta.replace('{dia_nombre}', fecha_actual.strftime('%A'))
            respuesta = respuesta.replace('{fecha_completa}', fecha_actual.strftime('%d de %B'))
        
        return respuesta
    
    return None

# Función para obtener respuesta contextual (por intereses)
def obtener_respuesta_contextual(categoria):
    """Obtiene respuesta contextual según interés del usuario"""
    respuestas_contextuales = RESPUESTA_FLUIDAS['respuestas_contextuales']
    
    if categoria in respuestas_contextuales:
        respuestas_list = respuestas_contextuales[categoria]['respuestas']
        return random.choice(respuestas_list)
    
    return None

# Función para normalizar texto
def normalizar_texto(texto):
    return texto.lower().strip()

# Función para buscar productos - MEJORADA para soportar nuevos campos del JSON
def buscar_productos(consulta):
    try:
        consulta = normalizar_texto(consulta)
        resultados = []
        
        # Buscar en nombre, descripción, categorías y palabras clave
        for prod in PRODUCTOS:
            try:
                nombre_lower = normalizar_texto(str(prod.get('nombre', '')))
                desc_lower = normalizar_texto(str(prod.get('descripcion', '')))
                cat_lower = normalizar_texto(str(prod.get('categoria', '')))
                
                # Buscar en campos estándar
                coincidencias_basicas = (
                    consulta in nombre_lower or 
                    consulta in desc_lower or 
                    consulta in cat_lower or
                    nombre_lower.startswith(consulta) or
                    cat_lower.startswith(consulta)
                )
                
                # Buscar en nuevos campos (si existen)
                coincidencias_avanzadas = False
                
                # Buscar en palabras clave
                if not coincidencias_avanzadas and 'palabras_clave' in prod and isinstance(prod['palabras_clave'], list):
                    palabras_norm = [normalizar_texto(str(p)) for p in prod['palabras_clave']]
                    coincidencias_avanzadas = any(consulta in palabra for palabra in palabras_norm)
                
                # Buscar en etiquetas de búsqueda
                if not coincidencias_avanzadas and 'etiquetas_busqueda' in prod and isinstance(prod['etiquetas_busqueda'], list):
                    etiquetas_norm = [normalizar_texto(str(e)) for e in prod['etiquetas_busqueda']]
                    coincidencias_avanzadas = any(consulta in etiqueta for etiqueta in etiquetas_norm)
                
                # Buscar en categorías secundarias
                if not coincidencias_avanzadas and 'categorias_secundarias' in prod and isinstance(prod['categorias_secundarias'], list):
                    cats_sec_norm = [normalizar_texto(str(c)) for c in prod['categorias_secundarias']]
                    coincidencias_avanzadas = any(consulta in cat_sec for cat_sec in cats_sec_norm)
                
                # Buscar en casos de uso
                if not coincidencias_avanzadas and 'casos_uso' in prod and isinstance(prod['casos_uso'], list):
                    casos_norm = [normalizar_texto(str(c)) for c in prod['casos_uso']]
                    coincidencias_avanzadas = any(consulta in caso for caso in casos_norm)
                
                # Buscar en público objetivo
                if not coincidencias_avanzadas and 'publico_objetivo' in prod and isinstance(prod['publico_objetivo'], list):
                    publicos_norm = [normalizar_texto(str(p)) for p in prod['publico_objetivo']]
                    coincidencias_avanzadas = any(consulta in publico for publico in publicos_norm)
                
                if coincidencias_basicas or coincidencias_avanzadas:
                    resultados.append(prod)
            except Exception:
                continue
        
        return resultados
    except Exception as e:
        return []

# Función para detectar intención del usuario
def detectar_intencion(mensaje):
    msg = normalizar_texto(mensaje)
    
    # Intención: Preguntas sobre el día/hora
    if any(word in msg for word in ['qué día', 'que dia', 'día de hoy', 'dia de hoy', 'qué hora', 'que hora', 'la hora', 'la fecha']):
        return 'fecha_hora'
    
    # Intención: Preguntas sobre el bot
    if any(word in msg for word in ['cómo estas', 'como estas', 'cómo estás', 'como estás', 'cómo va', 'como va', 'cómo te va', 'como te va', 'qué tal', 'que tal', 'de verdad']):
        return 'sobre_bot'
    
    # Intención: Nombre del bot
    if any(word in msg for word in ['tu nombre', 'quién eres', 'quien eres', 'cómo te llamas', 'como te llamas', 'cuál es tu nombre']):
        return 'nombre_bot'
    
    # Intención: Más recomendaciones (debe ir ANTES de búsqueda general)
    if any(word in msg for word in ['más', 'mas', 'otro', 'otra', 'diferente', 'más opciones', 'mas opciones', 'otras opciones', 'más cosas', 'mas cosas', '¿qué más?', 'que mas?', 'algo mas', 'algo más', 'algo diferente']):
        # Solo si no menciona un producto específico
        if not any(word in msg for word in ['laptop', 'mouse', 'teclado', 'monitor', 'iphone', 'ipad', 'auriculares', 'powerbank', 'gopro', 'samsung', 'corsair', 'logitech', 'asus', 'sony', 'lg', 'anker', 'xiaomi', 'msi', 'corsair']):
            return 'mas_recomendaciones'
    
    # Intención: Búsqueda
    if any(word in msg for word in ['busco', 'quiero', 'dame', 'necesito', 'tenéis', 'tienen', 'hay', 'mostrar', 'dónde está', 'donde esta', 'es decir', 'tienes']):
        return 'busqueda'
    
    # Intención: Precio
    if any(word in msg for word in ['precio', 'cuesta', 'cuánto', 'cuanto', 'vale', 'costo', 'caro', 'más barato']):
        return 'precio'
    
    # Intención: Carrito
    if any(word in msg for word in ['carrito', 'agregar', 'añadir', 'comprar', 'agrégame', 'añádeme']):
        return 'carrito'
    
    # Intención: Ver carrito
    if any(word in msg for word in ['mostrar carrito', 'ver carrito', 'qué tengo', 'mi carrito', 'mi compra', 'resumen']):
        return 'ver_carrito'
    
    # Intención: Limpiar carrito
    if any(word in msg for word in ['vaciar', 'limpiar', 'eliminar todo', 'borrar carrito', 'empezar de nuevo']):
        return 'limpiar_carrito'
    
    # Intención: Saludar
    if any(word in msg for word in ['hola', 'hi', 'buenos días', 'buenas noches', 'hey', 'oye', 'buenas tardes', 'buenos días']):
        return 'saludo'
    
    # Intención: Despedida
    if any(word in msg for word in ['adiós', 'adios', 'bye', 'hasta luego', 'chao', 'nos vemos', 'me voy', 'tengo que irme']):
        return 'despedida'
    
    # Intención: Ayuda
    if any(word in msg for word in ['ayuda', 'help', 'qué puedes', 'que puedes', 'qué haces', 'que haces', 'comandos', 'opciones']):
        return 'ayuda'
    
    # Intención: Gratitud
    if any(word in msg for word in ['gracias', 'grazie', 'thanks', 'muchas gracias', 'mucho', 'estupendo', 'perfecto']):
        return 'gratitud'
    
    # Intención: Broma/Conversación casual
    if any(word in msg for word in ['jaja', 'xd', 'lol', '😄', '😂', 'jajaja', 'jajaj']):
        return 'broma'
    
    # Intención: Conversación general
    if any(word in msg for word in ['eh', 'ok', 'bien', 'mal', 'muy bien', 'normal', 'igual', 'más o menos']):
        return 'conversacion_general'
    
    return 'otro'

# Función para extraer nombre de producto
def extraer_nombre_producto(mensaje):
    # Patrones comunes
    patrones = [
        r'(?:busco|quiero|dame|necesito|tenéis|tienen|hay|mostrar)\s+(.+?)(?:\?|$)',
        r'(?:el|la|un|una)\s+(.+?)(?:\?|$)',
        r'(?:precio|cuesta|vale|costo)\s+(?:del?|de la)\s+(.+?)(?:\?|$)'
    ]
    
    for patron in patrones:
        match = re.search(patron, normalizar_texto(mensaje))
        if match:
            return match.group(1).strip()
    
    return None

# NUEVA FUNCIÓN: Detectar múltiples productos en un mensaje
def extraer_multiples_productos(mensaje):
    """Busca múltiples productos mencionados en el mensaje"""
    msg_palabras = normalizar_texto(mensaje).split()
    productos_encontrados = []
    
    try:
        # Buscar cada palabra en los productos
        for palabra in msg_palabras:
            if len(palabra) > 2:  # Ignorar palabras muy cortas
                resultados = buscar_productos(palabra)
                if resultados:
                    # Agregar el primero que encuentre (más relevante)
                    prod_id = resultados[0].get('id')
                    existe = any(p.get('id') == prod_id for p in productos_encontrados)
                    if not existe:
                        productos_encontrados.append(resultados[0])
    except Exception as e:
        # Si hay error, retornar lista vacía
        return []
    
    return productos_encontrados

# Función para detectar intereses del usuario (palabras clave)
def extraer_intereses(mensaje):
    """Extrae palabras clave de manera MEJORADA buscando en múltiples campos del JSON"""
    try:
        msg = normalizar_texto(mensaje)
        intereses = []
        productos_coincidentes = []
        
        # Mapeo de palabras clave a categorías (fallback si JSON no tiene campos nuevos)
        mapeo_intereses_basico = {
            'gaming': ['gaming', 'juegos', 'gamer', 'fps', 'moba'],
            'trabajo': ['trabajo', 'oficina', 'laboral', 'productividad', 'negocios'],
            'viaje': ['viaje', 'portátil', 'compacto', 'ligero', 'mochila'],
            'fotografía': ['foto', 'fotografía', 'cámara', 'video', 'creador'],
            'audio': ['música', 'sonido', 'auricular', 'audio', 'podcast'],
            'portátil': ['portátil', 'ligero', 'ultrabook', 'delgado'],
            'potencia': ['potente', 'rápido', 'procesador', 'ram', 'performance'],
            'pantalla': ['pantalla', 'monitor', 'display', 'resolución'],
        }
        
        # Primero, buscar en productos usando nuevos campos
        for producto in PRODUCTOS:
            try:
                # Compilar todas las claves disponibles en el producto
                todas_las_claves = []
                
                # Agregar campos estándar
                todas_las_claves.append(normalizar_texto(str(producto.get('nombre', ''))))
                todas_las_claves.append(normalizar_texto(str(producto.get('categoria', ''))))
                todas_las_claves.append(normalizar_texto(str(producto.get('descripcion', ''))))
                
                # Agregar nuevos campos si existen
                if 'palabras_clave' in producto and isinstance(producto['palabras_clave'], list):
                    todas_las_claves.extend([normalizar_texto(str(p)) for p in producto['palabras_clave']])
                
                if 'etiquetas_busqueda' in producto and isinstance(producto['etiquetas_busqueda'], list):
                    todas_las_claves.extend([normalizar_texto(str(e)) for e in producto['etiquetas_busqueda']])
                
                if 'categorias_secundarias' in producto and isinstance(producto['categorias_secundarias'], list):
                    todas_las_claves.extend([normalizar_texto(str(c)) for c in producto['categorias_secundarias']])
                
                if 'casos_uso' in producto and isinstance(producto['casos_uso'], list):
                    todas_las_claves.extend([normalizar_texto(str(c)) for c in producto['casos_uso']])
                
                if 'publico_objetivo' in producto and isinstance(producto['publico_objetivo'], list):
                    todas_las_claves.extend([normalizar_texto(str(p)) for p in producto['publico_objetivo']])
                
                # Buscar coincidencias
                if any(clave in msg for clave in todas_las_claves):
                    productos_coincidentes.append(producto)
                    # Extraer categorías del producto coincidente
                    if 'categorias_secundarias' in producto:
                        intereses.extend(producto['categorias_secundarias'])
                    else:
                        intereses.append(producto.get('categoria', 'general'))
            except Exception:
                continue
        
        # Si no encontró nada en productos, usar mapeo básico
        if not intereses:
            for categoria, palabras in mapeo_intereses_basico.items():
                if any(palabra in msg for palabra in palabras):
                    intereses.append(categoria)
        
        # Retornar intereses únicos
        return list(set(intereses))
    
    except Exception as e:
        # Si algo falla, retornar lista vacía
        return []

# Mapeo avanzado de intereses a productos con prioridades
MAPEO_INTERESES_AVANZADO = {
    'gaming': {
        'periféricos': [5, 6],  # Teclado, Mouse
        'móvil': [2],  # iPhone
        'audio': [9],  # Sony Headphones
        'monitor': [4],  # Monitor
    },
    'trabajo': {
        'monitor': [4],  # Monitor LG
        'periféricos': [6],  # Mouse
        'portátil': [7],  # iPad
        'potencia': [1],  # Laptop
    },
    'viaje': {
        'portátil': [1, 7],  # Laptop, iPad
        'batería': [10],  # PowerBank
        'móvil': [2],  # iPhone
    },
    'fotografía': {
        'cámara': [8],  # GoPro
        'portátil': [1],  # Laptop para editar
        'almacenamiento': [10],  # PowerBank
    },
    'audio': {
        'auriculares': [3, 9],  # Galaxy Buds, Sony
        'móvil': [2],  # iPhone
    },
    'portátil': {
        'laptop': [1],  # Laptop ASUS
        'batería': [10],  # PowerBank
    },
    'potencia': {
        'laptop': [1],  # Laptop ASUS
        'monitor': [4],  # Monitor
        'ram': [7],  # iPad
    },
    'pantalla': {
        'monitor': [4],  # Monitor
    },
}

# Mapeo de complementos (si tiene X, recomienda Y)
COMPLEMENTOS_INTELIGENTES = {
    1: [10, 6, 4],  # Laptop → PowerBank, Mouse, Monitor
    2: [3, 9],  # iPhone → Galaxy Buds, Sony
    3: [2],  # Galaxy Buds → iPhone
    4: [6],  # Monitor → Mouse
    5: [6],  # Teclado → Mouse
    6: [5],  # Mouse → Teclado
    7: [6, 4],  # iPad → Mouse, Monitor
    8: [1],  # GoPro → Laptop
    9: [2],  # Sony → iPhone
    10: [1, 2],  # PowerBank → Laptop, iPhone
}

# Palabras clave específicas para cada tipo de necesidad
PALABRAS_CLAVE_ESPECIFICAS = {
    'portátil': ['portátil', 'ultrabook', 'delgado', 'ligero', 'móvil', 'viaje'],
    'potencia': ['rápido', 'potente', 'procesador', 'ram', 'multitarea', 'pesado'],
    'pantalla': ['pantalla', 'display', 'monitor', 'resolución', 'colores'],
    'audio': ['sonido', 'música', 'podcast', 'audio', 'auricular', 'ruido'],
    'edición': ['video', 'edición', 'contenido', 'creador', 'foto'],
    'profesional': ['trabajo', 'oficina', 'reunión', 'productividad', 'empresarial'],
}

def analizar_conversacion_profunda(historial_mensajes):
    """Analiza el historial de conversación para entender necesidades del usuario"""
    if not historial_mensajes:
        return {}
    
    conversacion_completa = ' '.join(historial_mensajes).lower()
    
    # Analizar patrones de conversación
    analisis = {
        'mentalidad_usuario': 'indefinida',
        'nivel_urgencia': 'normal',
        'presupuesto': 'flexible',
        'necesidades_especiales': [],
        'tipo_uso': [],
        'frecuencia_compra': 'primera_vez'
    }
    
    # Detectar mentalidad (gamer, profesional, viajero, etc.)
    if any(word in conversacion_completa for word in ['gamer', 'juegos', 'fps', 'rank', 'competitivo']):
        analisis['mentalidad_usuario'] = 'gamer'
    elif any(word in conversacion_completa for word in ['trabajo', 'oficina', 'reunión', 'empresa']):
        analisis['mentalidad_usuario'] = 'profesional'
    elif any(word in conversacion_completa for word in ['viaje', 'nómada', 'portátil', 'ligero']):
        analisis['mentalidad_usuario'] = 'viajero'
    elif any(word in conversacion_completa for word in ['foto', 'video', 'contenido', 'creador']):
        analisis['mentalidad_usuario'] = 'creador'
    
    # Detectar urgencia
    if any(word in conversacion_completa for word in ['urgente', 'ahora', 'inmediato', 'rápido']):
        analisis['nivel_urgencia'] = 'alta'
    
    # Detectar presupuesto
    if any(word in conversacion_completa for word in ['caro', 'premium', 'mejor', 'top']):
        analisis['presupuesto'] = 'alto'
    elif any(word in conversacion_completa for word in ['barato', 'económico', 'presupuesto']):
        analisis['presupuesto'] = 'bajo'
    
    # Detectar necesidades especiales
    for necesidad, palabras in PALABRAS_CLAVE_ESPECIFICAS.items():
        if any(palabra in conversacion_completa for palabra in palabras):
            analisis['necesidades_especiales'].append(necesidad)
    
    return analisis

def recomendar_productos_inteligente(intereses, carrito_actual, historial_mensajes=None, limite=3):
    """Recomendación inteligente basada en intereses, conversación y complementos - VERSIÓN MEJORADA"""
    try:
        if not intereses:
            return []
        
        # Obtener IDs de productos ya en carrito
        ids_carrito = {item.get('id') for item in carrito_actual}
        
        # Calcular puntuación de cada producto
        puntuaciones = {}
        
        # ESTRATEGIA 1: Buscar productos que compartan categorías secundarias
        for producto in PRODUCTOS:
            if producto.get('id') in ids_carrito:
                continue
            
            try:
                prod_categorias = producto.get('categorias_secundarias', [])
                prod_categoria_principal = producto.get('categoria_principal', '')
                
                # Calcular coincidencias
                coincidencias = 0
                for interes in intereses:
                    # Buscar en categorías secundarias
                    if interes.lower() in [c.lower() for c in prod_categorias]:
                        coincidencias += 3
                    # Buscar en categoría principal
                    if interes.lower() in prod_categoria_principal.lower():
                        coincidencias += 2
                    # Buscar en palabras clave
                    if 'palabras_clave' in producto:
                        if interes.lower() in [p.lower() for p in producto['palabras_clave']]:
                            coincidencias += 2
                    # Buscar en casos de uso
                    if 'casos_uso' in producto:
                        if interes.lower() in [c.lower() for c in producto['casos_uso']]:
                            coincidencias += 1
                    # Buscar en público objetivo
                    if 'publico_objetivo' in producto:
                        if interes.lower() in [p.lower() for p in producto['publico_objetivo']]:
                            coincidencias += 1
                
                if coincidencias > 0:
                    puntuaciones[producto.get('id')] = coincidencias
            except Exception:
                continue
        
        # ESTRATEGIA 2: Agregar complementos inteligentes (basados en carrito actual)
        for item in carrito_actual:
            item_id = item.get('id')
            if item_id in COMPLEMENTOS_INTELIGENTES:
                complementos = COMPLEMENTOS_INTELIGENTES[item_id]
                for comp_id in complementos:
                    if comp_id not in ids_carrito:
                        puntuaciones[comp_id] = puntuaciones.get(comp_id, 0) + 5
        
        # ESTRATEGIA 3: Si no hay suficientes recomendaciones, agregar productos similares por categoría
        if len(puntuaciones) < limite:
            for producto in PRODUCTOS:
                if producto.get('id') in ids_carrito or producto.get('id') in puntuaciones:
                    continue
                try:
                    # Buscar por categoría principal
                    for interes in intereses:
                        if interes.lower() in producto.get('categoria_principal', '').lower():
                            puntuaciones[producto.get('id')] = puntuaciones.get(producto.get('id'), 0) + 1
                except Exception:
                    continue
        
        # Ordenar por puntuación
        productos_ordenados = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
        
        # Obtener objetos de producto
        resultado = []
        for pid, puntuacion in productos_ordenados[:limite]:
            for prod in PRODUCTOS:
                if prod.get('id') == pid:
                    resultado.append(prod)
                    break
        
        return resultado
    
    except Exception as e:
        return []

# Mantener función antigua para compatibilidad
def recomendar_productos(intereses, carrito_actual, limite=3):
    """Recomendación básica (compatibilidad)"""
    # Mapeo de intereses a categorías de productos
    recomendaciones = {
        'gaming': [5, 2],  # Teclado, iPhone
        'trabajo': [4, 6, 7],  # Monitor, Mouse, iPad
        'viaje': [1, 10],  # Laptop, PowerBank
        'fotografía': [8],  # GoPro
        'audio': [3, 9],  # Galaxy Buds, Sony Headphones
        'portátil': [1, 10],  # Laptop, PowerBank
        'potencia': [1, 4],  # Laptop, Monitor
        'pantalla': [4],  # Monitor
    }
    
    productos_recomendados = set()
    for interes in intereses:
        if interes in recomendaciones:
            productos_recomendados.update(recomendaciones[interes])
    
    # Filtrar productos ya en carrito
    ids_carrito = [item['id'] for item in carrito_actual]
    productos_id = [pid for pid in productos_recomendados if pid not in ids_carrito]
    
    # Obtener objetos de producto
    resultado = []
    for pid in productos_id[:limite]:
        for prod in PRODUCTOS:
            if prod['id'] == pid:
                resultado.append(prod)
                break
    
    return resultado

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# API para mensajes del chat
@app.route('/api/chat', methods=['POST'])
def chat():
    datos = request.json
    mensaje_usuario = datos.get('mensaje', '').strip()
    
    if not mensaje_usuario:
        return jsonify({'error': 'Mensaje vacío'}), 400
    
    # Inicializar carrito en sesión si no existe
    if 'carrito' not in session:
        session['carrito'] = []
    
    # Inicializar historial de mensajes para contexto
    if 'historial' not in session:
        session['historial'] = []
    
    # Agregar mensaje al historial
    session['historial'].append(mensaje_usuario)
    session['historial'] = session['historial'][-10:]  # Mantener últimos 10 mensajes
    
    intencion = detectar_intencion(mensaje_usuario)
    respuesta = generar_respuesta(mensaje_usuario, intencion, session['carrito'], session['historial'])
    
    # Guardar sesión si hay cambios
    session.modified = True
    
    return jsonify({
        'respuesta': respuesta['texto'],
        'intencion': intencion,
        'productos': respuesta.get('productos', []),
        'carrito': session.get('carrito', []),
        'timestamp': datetime.now().isoformat()
    })

# Función para generar respuesta
def generar_respuesta(mensaje, intencion, carrito, historial=None):
    if intencion == 'saludo':
        # Detectar intereses incluso en el saludo (mejorado)
        intereses = extraer_intereses(mensaje)
        respuesta_random = obtener_respuesta('saludo') or "¡Hola! Bienvenido"
        
        if intereses:
            # Agregar respuesta contextual según interés detectado
            respuesta_contextual = obtener_respuesta_contextual(intereses[0])
            if respuesta_contextual:
                respuesta_random += "\n\n" + respuesta_contextual
            
            recomendados = recomendar_productos_inteligente(intereses, carrito, historial)
            if recomendados:
                respuesta_random += "\n\n💡 **Productos que podrían interesarte:**"
                for prod in recomendados[:3]:
                    respuesta_random += f"\n• **{prod['nombre']}** - ${prod['precio']}"
                return {'texto': respuesta_random, 'productos': recomendados}
        
        return {'texto': respuesta_random}
    
    elif intencion == 'mas_recomendaciones':
        # Usuario quiere más opciones/recomendaciones
        intereses = extraer_intereses(mensaje)  # Mejorado para buscar en todos los campos
        
        # Si no hay intereses previos, ofrecer todas las categorías
        if not intereses:
            respuesta = "¡Claro! Aquí tengo más opciones para ti:\n\n💡 **Variedad de productos:**"
            # Mostrar productos variados
            productos_muestra = random.sample(PRODUCTOS, min(5, len(PRODUCTOS)))
            for prod in productos_muestra:
                respuesta += f"\n• **{prod['nombre']}** - ${prod['precio']}"
            return {'texto': respuesta, 'productos': productos_muestra}
        
        # Si hay intereses, recomendar basado en contexto
        respuesta = "¡Perfecto! Aquí tienes más opciones que te pueden interesar:\n\n"
        recomendados = recomendar_productos_inteligente(intereses, carrito, historial, 5)
        
        if recomendados:
            respuesta += "💡 **Alternativas basadas en tu interés:**"
            for prod in recomendados:
                respuesta += f"\n• **{prod['nombre']}** - ${prod['precio']}"
            return {'texto': respuesta, 'productos': recomendados}
        else:
            # Si no encuentra recomendaciones, mostrar variados
            productos_muestra = random.sample(PRODUCTOS, min(5, len(PRODUCTOS)))
            respuesta = "Aquí tienes variedad de productos:\n\n"
            for prod in productos_muestra:
                respuesta += f"\n• **{prod['nombre']}** - ${prod['precio']}"
            return {'texto': respuesta, 'productos': productos_muestra}
    
    elif intencion == 'despedida':
        return {'texto': obtener_respuesta('despedida') or "¡Hasta luego!"}
    
    elif intencion == 'fecha_hora':
        return {'texto': obtener_respuesta('fecha_hora')}
    
    elif intencion == 'sobre_bot':
        return {'texto': obtener_respuesta('sobre_bot') or "¡Estoy perfecto!"}
    
    elif intencion == 'nombre_bot':
        return {'texto': obtener_respuesta('nombre_bot') or "Soy TechBot"}
    
    elif intencion == 'gratitud':
        return {'texto': obtener_respuesta('gratitud') or "¡De nada!"}
    
    elif intencion == 'broma':
        return {'texto': obtener_respuesta('bromas') or "¡Jajaja!"}
    
    elif intencion == 'conversacion_general':
        # Extraer intereses y recomendar (mejorado)
        intereses = extraer_intereses(mensaje)
        respuestas_general = obtener_respuesta('conversacion_general') or "Interesante..."
        
        if intereses:
            # Agregar respuesta contextual
            respuesta_contextual = obtener_respuesta_contextual(intereses[0])
            if respuesta_contextual:
                respuestas_general += "\n\n" + respuesta_contextual
            
            recomendados = recomendar_productos_inteligente(intereses, carrito, historial)
            if recomendados:
                respuestas_general += f"\n\n💡 **Te podría interesar:**"
                for prod in recomendados[:3]:
                    respuestas_general += f"\n• **{prod['nombre']}** - ${prod['precio']}"
                return {'texto': respuestas_general, 'productos': recomendados}
        else:
            # Si no hay intereses detectados, mostrar algunos productos aleatorios
            productos_aleatorios = random.sample(PRODUCTOS, min(3, len(PRODUCTOS)))
            respuestas_general += f"\n\n💡 **Productos que te pueden interesar:**"
            for prod in productos_aleatorios:
                respuestas_general += f"\n• **{prod['nombre']}** - ${prod['precio']}"
            return {'texto': respuestas_general, 'productos': productos_aleatorios}
        
        return {'texto': respuestas_general}
    
    elif intencion == 'ayuda':
        ayuda_texto = """
        Aquí está lo que puedo hacer por ti:
        
        🔍 **Buscar productos**: "Busco un laptop" o "Tenéis auriculares?"
        💰 **Precios**: "¿Cuánto cuesta el iPhone?"
        🛒 **Comprar**: "Agrégame el iPhone al carrito"
        📋 **Ver carrito**: "Mostrar mi carrito"
        🗑️ **Vaciar carrito**: "Limpiar mi carrito"
        ⏰ **Hora/Fecha**: "¿Qué día es?" o "¿Qué hora es?"
        🤖 **Sobre mí**: "¿Cómo estás?" o "¿Cuál es tu nombre?"
        💬 **Conversa conmigo**: ¡Puedo charlar de cualquier cosa!
        
        ¿En qué puedo ayudarte?
        """
        return {'texto': ayuda_texto}
    
    elif intencion == 'busqueda':
        nombre = extraer_nombre_producto(mensaje)
        if not nombre:
            return {'texto': obtener_respuesta('busqueda') or "¿Qué producto específico te interesa? 🔍"}
        
        resultados = buscar_productos(nombre)
        
        if not resultados:
            # Si no encuentra exacto, intenta con recomendaciones basadas en intereses (mejorado)
            intereses = extraer_intereses(mensaje)
            recomendados = recomendar_productos_inteligente(intereses, carrito, historial, 3) if intereses else []
            
            if recomendados:
                texto_respuesta = f"No encontré exactamente '{nombre}' 😕\n\nPero te recomiendo estos productos similares:\n\n"
                for prod in recomendados:
                    texto_respuesta += f"• **{prod['nombre']}** - ${prod['precio']}\n  {prod['descripcion']}\n\n"
                return {'texto': texto_respuesta, 'productos': recomendados}
            
            return {'texto': f"Hmm, no encontré '{nombre}' 😕 ¿Quizás buscas otra cosa? ¿Necesitas ayuda? 🔍"}
        
        texto_respuesta = obtener_respuesta('busqueda') or f"¡Genial! Encontré productos:\n\n"
        texto_respuesta += f"Encontré {len(resultados)} producto(s) relacionado(s) con '{nombre}':\n\n"
        for prod in resultados:
            texto_respuesta += f"• **{prod['nombre']}** - ${prod['precio']}\n  {prod['descripcion']}\n\n"
        
        # Sugerir productos relacionados (mejorado)
        intereses = extraer_intereses(nombre + " " + str(resultados))
        if intereses:
            otros = recomendar_productos_inteligente(intereses, carrito + [{'id': r['id']} for r in resultados], historial, 1)
            if otros:
                texto_respuesta += f"💡 **También te podría interesar:** {otros[0]['nombre']} (${otros[0]['precio']}) - Perfecta combinación\n\n"
        
        texto_respuesta += "¿Te interesa alguno? 😊"
        
        return {
            'texto': texto_respuesta,
            'productos': resultados
        }
    
    elif intencion == 'precio':
        nombre = extraer_nombre_producto(mensaje)
        if not nombre:
            return {'texto': obtener_respuesta('precio') or "¿De cuál producto quieres saber el precio? 💰"}
        
        resultados = buscar_productos(nombre)
        
        if not resultados:
            return {'texto': f"No encontré '{nombre}' en nuestro inventario 😞"}
        
        texto_respuesta = ""
        for prod in resultados:
            texto_respuesta += f"El **{prod['nombre']}** cuesta **${prod['precio']}** 💵\n"
        
        return {'texto': texto_respuesta, 'productos': resultados}
    
    elif intencion == 'carrito':
        # Intentar extraer múltiples productos primero
        productos_multiples = extraer_multiples_productos(mensaje)
        
        if productos_multiples:
            # Agregar múltiples productos al carrito
            productos_agregados = []
            productos_duplicados = []
            
            for producto in productos_multiples:
                item_carrito = {
                    'id': producto['id'],
                    'nombre': producto['nombre'],
                    'precio': producto['precio']
                }
                
                # Verificar si ya está en carrito
                existe = any(item['id'] == producto['id'] for item in carrito)
                
                if existe:
                    productos_duplicados.append(producto['nombre'])
                else:
                    carrito.append(item_carrito)
                    productos_agregados.append(producto)
            
            # Construir respuesta
            respuesta = ""
            
            if productos_agregados:
                respuesta = f"✅ ¡Perfecto! Agregué {len(productos_agregados)} producto(s):\n\n"
                for prod in productos_agregados:
                    respuesta += f"• {prod['nombre']} (${prod['precio']})\n"
            
            if productos_duplicados:
                respuesta += f"\n⚠️ Estos ya estaban en tu carrito:\n"
                for nombre in productos_duplicados:
                    respuesta += f"• {nombre}\n"
            
            total = sum(item['precio'] for item in carrito)
            respuesta += f"\n📊 Total actual: **${total:.2f}**\n\n¿Necesitas algo más? 😊"
            
            return {'texto': respuesta}
        
        # Si no encuentra múltiples, intenta extraer uno solo
        nombre = extraer_nombre_producto(mensaje)
        if not nombre:
            return {'texto': obtener_respuesta('carrito') or "¿Cuál producto quieres agregar al carrito? 🛒"}
        
        resultados = buscar_productos(nombre)
        
        if not resultados:
            return {'texto': f"No encontré '{nombre}' 😕"}
        
        producto = resultados[0]
        item_carrito = {
            'id': producto['id'],
            'nombre': producto['nombre'],
            'precio': producto['precio']
        }
        
        # Verificar si ya está en carrito
        existe = any(item['id'] == producto['id'] for item in carrito)
        
        if existe:
            return {'texto': f"✓ '{producto['nombre']}' ya está en tu carrito 📦"}
        
        carrito.append(item_carrito)
        total = sum(item['precio'] for item in carrito)
        
        respuesta = obtener_respuesta('carrito') or f"✅ ¡Perfecto! Agregué '{producto['nombre']}'"
        respuesta = f"✅ ¡Perfecto! Agregué '{producto['nombre']}' (${producto['precio']}) a tu carrito.\n\n📊 Total actual: **${total:.2f}**"
        
        # Sugerir complementos (mejorado con campos nuevos)
        intereses = extraer_intereses(producto['nombre'] + " " + producto['descripcion'])
        if intereses:
            respuesta_contextual = obtener_respuesta_contextual(intereses[0])
            if respuesta_contextual:
                respuesta += "\n\n" + respuesta_contextual
            
            otros = recomendar_productos_inteligente(intereses, carrito, historial, 2)
            if otros:
                respuesta += "\n\n💡 **Productos que combinan bien:**"
                for prod in otros:
                    respuesta += f"\n• {prod['nombre']} (${prod['precio']}) - Perfecto para ti"
        
        respuesta += "\n\n¿Necesitas algo más? 😊"
        
        return {'texto': respuesta}
    
    elif intencion == 'ver_carrito':
        if not carrito:
            return {'texto': obtener_respuesta('ver_carrito') or "Tu carrito está vacío 😕 ¿Te gustaría buscar algo? 🔍"}
        
        texto_respuesta = "📦 **Tu carrito:**\n\n"
        total = 0
        for idx, item in enumerate(carrito, 1):
            texto_respuesta += f"{idx}. {item['nombre']} - ${item['precio']}\n"
            total += item['precio']
        
        texto_respuesta += f"\n💰 **Total**: ${total:.2f}\n\n¿Deseas proceder al pago o agregar más productos? 🛍️"
        
        return {'texto': texto_respuesta}
    
    elif intencion == 'limpiar_carrito':
        if not carrito:
            return {'texto': "Tu carrito ya está vacío 😊"}
        
        carrito.clear()
        return {'texto': obtener_respuesta('limpiar_carrito') or "🗑️ Carrito vaciado. ¿Hay algo más que pueda ayudarte? 😊"}
    
    else:
        # Respuestas más conversacionales CON sugerencias (mejorado)
        intereses = extraer_intereses(mensaje)
        respuestas_otro = obtener_respuesta('no_entiendo') or "Interesante... pero no estoy muy seguro."
        
        respuesta = respuestas_otro
        
        # Si detecta intereses, sugerir productos basados en eso
        if intereses:
            # Agregar respuesta contextual
            respuesta_contextual = obtener_respuesta_contextual(intereses[0])
            if respuesta_contextual:
                respuesta += "\n\n" + respuesta_contextual
            
            recomendados = recomendar_productos_inteligente(intereses, carrito, historial, 3)
            if recomendados:
                respuesta += "\n\n💡 **Basándome en lo que dijiste, te recomiendo:**"
                for prod in recomendados:
                    respuesta += f"\n• **{prod['nombre']}** - ${prod['precio']}"
                return {'texto': respuesta, 'productos': recomendados}
        else:
            # Si no detecta intereses, mostrar productos variados
            productos_variados = random.sample(PRODUCTOS, min(3, len(PRODUCTOS)))
            respuesta += "\n\n💡 **Aquí tengo algunos productos que podrían interesarte:**"
            for prod in productos_variados:
                respuesta += f"\n• **{prod['nombre']}** - ${prod['precio']}"
            return {'texto': respuesta, 'productos': productos_variados}
        
        return {'texto': respuesta}

# Ruta para obtener lista de productos
@app.route('/api/productos', methods=['GET'])
def get_productos():
    return jsonify(PRODUCTOS)

# Ruta para sesiones
@app.route('/api/session', methods=['GET'])
def get_session():
    return jsonify({'carrito': session.get('carrito', [])})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
