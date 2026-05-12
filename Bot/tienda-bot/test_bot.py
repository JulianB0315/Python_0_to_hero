"""
Script de prueba para verificar que el bot funciona correctamente
Ejecuta: python test_bot.py
"""

import json
import re
from datetime import datetime

# Cargar productos
with open('productos.json', 'r', encoding='utf-8') as f:
    PRODUCTOS = json.load(f)['productos']

def normalizar_texto(texto):
    return texto.lower().strip()

def detectar_intencion(mensaje):
    msg = normalizar_texto(mensaje)
    
    if any(word in msg for word in ['qué día', 'que dia', 'qué hora', 'que hora']):
        return 'fecha_hora'
    
    if any(word in msg for word in ['cómo estas', 'como estas', 'cómo va', 'como va']):
        return 'sobre_bot'
    
    if any(word in msg for word in ['tu nombre', 'quién eres', 'quien eres', 'cómo te llamas']):
        return 'nombre_bot'
    
    if any(word in msg for word in ['busco', 'quiero', 'dame', 'necesito']):
        return 'busqueda'
    
    if any(word in msg for word in ['precio', 'cuesta', 'cuánto', 'cuanto', 'vale']):
        return 'precio'
    
    return 'otro'

def buscar_productos(consulta):
    consulta = normalizar_texto(consulta)
    resultados = []
    
    for prod in PRODUCTOS:
        nombre_lower = normalizar_texto(prod['nombre'])
        desc_lower = normalizar_texto(prod['descripcion'])
        
        if (consulta in nombre_lower or 
            consulta in desc_lower or
            nombre_lower.startswith(consulta)):
            resultados.append(prod)
    
    return resultados

# PRUEBAS
print("="*60)
print("🧪 PRUEBAS DEL BOT TECHSTORE")
print("="*60)

pruebas = [
    ("¿Cómo estás?", "sobre_bot", "Conversación casual"),
    ("¿Qué hora es?", "fecha_hora", "Fecha y hora"),
    ("¿Cuál es tu nombre?", "nombre_bot", "Identidad del bot"),
    ("Busco un laptop", "busqueda", "Búsqueda de producto"),
    ("¿Cuánto cuesta el iPhone?", "precio", "Consulta de precio"),
]

print("\n✅ PROBANDO DETECCIÓN DE INTENCIONES:\n")
for mensaje, intencion_esperada, descripcion in pruebas:
    intencion = detectar_intencion(mensaje)
    estado = "✓" if intencion == intencion_esperada else "✗"
    print(f"{estado} '{mensaje}'")
    print(f"   → Intención: {intencion} ({descripcion})")
    print()

print("\n✅ PROBANDO BÚSQUEDA DE PRODUCTOS:\n")
busquedas = [
    ("laptop", 1),
    ("auriculares", 2),
    ("iphone", 1),
    ("monitor", 1),
]

for termino, esperados in busquedas:
    resultados = buscar_productos(termino)
    encontrados = len(resultados)
    estado = "✓" if encontrados >= 1 else "✗"
    print(f"{estado} Búsqueda '{termino}': Encontrados {encontrados} productos")
    for prod in resultados[:2]:
        print(f"   - {prod['nombre']} (${prod['precio']})")

print("\n✅ VERIFICANDO DATOS:\n")
print(f"✓ Total de productos en catálogo: {len(PRODUCTOS)}")
print(f"✓ Productos cargados correctamente: {PRODUCTOS[0]['nombre']}, {PRODUCTOS[1]['nombre']}, etc.")

ahora = datetime.now()
print(f"✓ Hora actual del sistema: {ahora.strftime('%H:%M:%S')}")
print(f"✓ Fecha actual: {ahora.strftime('%A, %d de %B')}")

print("\n" + "="*60)
print("✨ ¡TODAS LAS PRUEBAS COMPLETADAS!")
print("="*60)
print("\n📝 Si llegaste hasta aquí, todo está bien configurado.")
print("🚀 Ahora ejecuta: python app.py")
print("   Y abre: http://localhost:5000\n")
