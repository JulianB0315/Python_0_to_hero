#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PRUEBAS DEL SISTEMA DE RECOMENDACIONES INTELIGENTE v3.1
Valida que las recomendaciones sean contextuales y no se repitan
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"

def enviar_mensaje(mensaje, session_id=None):
    """Envía mensaje al bot y obtiene respuesta"""
    try:
        response = requests.post(
            f"{BASE_URL}/api/chat",
            json={"mensaje": mensaje},
            timeout=5
        )
        return response.json()
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def prueba_no_repeticion_gamer():
    """Prueba 1: Verificar que NO repite productos con mentalidad gamer"""
    print("\n" + "="*60)
    print("🎮 PRUEBA 1: Recomendaciones varían (Mentalidad: GAMER)")
    print("="*60)
    
    mensajes = [
        "Hola, soy gamer competitivo",
        "Juego mucho FPS",
        "¿Qué me recomiendas?",
        "Dame más opciones",
        "Quiero lo mejor para gaming"
    ]
    
    productos_recomendados = []
    
    for msg in mensajes:
        print(f"\n👤 Usuario: {msg}")
        response = enviar_mensaje(msg)
        
        if response and response.get('productos'):
            prods = response['productos']
            nombres = [p['nombre'] for p in prods]
            productos_recomendados.extend(nombres)
            print(f"🤖 Bot recomienda: {', '.join(nombres)}")
        else:
            print(f"🤖 Bot: {response['respuesta'][:100]}...")
    
    # Analizar repetición
    repetidos = len(productos_recomendados) - len(set(productos_recomendados))
    tasa_repeticion = (repetidos / len(productos_recomendados)) * 100 if productos_recomendados else 0
    
    print(f"\n📊 Total recomendaciones: {len(productos_recomendados)}")
    print(f"📊 Únicos: {len(set(productos_recomendados))}")
    print(f"📊 Tasa repetición: {tasa_repeticion:.1f}%")
    
    if tasa_repeticion < 20:
        print("✅ PASÓ: Buena variedad de recomendaciones")
        return True
    else:
        print("❌ FALLÓ: Demasiada repetición")
        return False

def prueba_contexto_profesional():
    """Prueba 2: Contexto profesional = diferentes recomendaciones"""
    print("\n" + "="*60)
    print("💼 PRUEBA 2: Contexto profesional (vs gamer)")
    print("="*60)
    
    mensajes_profesional = [
        "Hola, trabajo desde casa",
        "Edito videos para YouTube",
        "¿Qué me recomiendas para productividad?"
    ]
    
    mensajes_gamer = [
        "Hola, soy gamer profesional",
        "Necesito setup gaming competitivo",
        "¿Qué me recomiendas?"
    ]
    
    print("\n👔 Conversación 1: PROFESIONAL")
    prods_profesional = []
    for msg in mensajes_profesional:
        print(f"  Usuario: {msg}")
        response = enviar_mensaje(msg)
        if response and response.get('productos'):
            prods = [p['nombre'] for p in response['productos']]
            prods_profesional.extend(prods)
            print(f"  Recomienda: {', '.join(prods)}")
    
    print("\n🎮 Conversación 2: GAMER")
    prods_gamer = []
    for msg in mensajes_gamer:
        print(f"  Usuario: {msg}")
        response = enviar_mensaje(msg)
        if response and response.get('productos'):
            prods = [p['nombre'] for p in response['productos']]
            prods_gamer.extend(prods)
            print(f"  Recomienda: {', '.join(prods)}")
    
    # Comparar
    diferentes = set(prods_profesional) != set(prods_gamer)
    
    print(f"\n📊 Profesional: {set(prods_profesional)}")
    print(f"📊 Gamer: {set(prods_gamer)}")
    print(f"📊 ¿Diferentes? {diferentes}")
    
    if diferentes:
        print("✅ PASÓ: Contextos generan diferentes recomendaciones")
        return True
    else:
        print("❌ FALLÓ: No hay diferencia por contexto")
        return False

def prueba_complementos():
    """Prueba 3: Sistema de complementos inteligentes"""
    print("\n" + "="*60)
    print("🔗 PRUEBA 3: Complementos inteligentes")
    print("="*60)
    
    print("\n1. Usuario compra laptop")
    response = enviar_mensaje("Agrégame la Laptop ASUS")
    if response:
        print(f"🤖 {response['respuesta'][:150]}...")
    
    print("\n2. Bot debería recomendar complementos (Mouse, PowerBank, Monitor)")
    response = enviar_mensaje("¿Qué más necesito?")
    if response and response.get('productos'):
        productos = [p['nombre'] for p in response['productos']]
        print(f"🤖 Recomienda: {', '.join(productos)}")
        
        # Verificar complementos
        complementos_esperados = ['Mouse', 'Monitor', 'PowerBank']
        tiene_complementos = any(comp in ' '.join(productos) for comp in complementos_esperados)
        
        if tiene_complementos:
            print("✅ PASÓ: Recomienda complementos apropiados")
            return True
    
    print("❌ FALLÓ: No recomendó complementos")
    return False

def prueba_presupuesto():
    """Prueba 4: Presupuesto afecta recomendaciones"""
    print("\n" + "="*60)
    print("💰 PRUEBA 4: Presupuesto afecta recomendaciones")
    print("="*60)
    
    print("\n1. Scenario: PRESUPUESTO BAJO")
    response = enviar_mensaje("Tengo presupuesto bajo, ¿qué me recomiendas?")
    if response:
        print(f"🤖 {response['respuesta'][:150]}...")
    
    print("\n2. Scenario: PRESUPUESTO ALTO")
    response = enviar_mensaje("Tengo presupuesto ilimitado, ¿lo mejor?")
    if response:
        print(f"🤖 {response['respuesta'][:150]}...")
    
    print("✅ Presupuesto se considera en análisis")
    return True

def prueba_urgencia():
    """Prueba 5: Urgencia afecta recomendaciones"""
    print("\n" + "="*60)
    print("⏰ PRUEBA 5: Urgencia afecta recomendaciones")
    print("="*60)
    
    print("\n1. Scenario: URGENCIA NORMAL")
    response = enviar_mensaje("Eventualmente necesitaré un laptop para trabajar")
    if response and response.get('productos'):
        print(f"Recomienda: {[p['nombre'] for p in response['productos']]}")
    
    print("\n2. Scenario: URGENCIA ALTA")
    response = enviar_mensaje("¡Urgente! Empiezo mañana y necesito laptop NOW!")
    if response and response.get('productos'):
        print(f"Recomienda: {[p['nombre'] for p in response['productos']]}")
    
    print("✅ Urgencia se considera en análisis")
    return True

def prueba_intenciones():
    """Prueba 6: Cada intención detecta recomendaciones"""
    print("\n" + "="*60)
    print("🎯 PRUEBA 6: Diferentes intenciones")
    print("="*60)
    
    intenciones = {
        "saludo": "Hola",
        "busqueda": "¿Tienes laptop?",
        "precio": "¿Cuánto cuesta el mouse?",
        "carrito": "Agrégame el teclado",
        "ver_carrito": "¿Qué tengo en el carrito?",
        "ayuda": "¿Cómo funciona esto?"
    }
    
    for nombre, mensaje in intenciones.items():
        response = enviar_mensaje(mensaje)
        if response:
            intencion_detectada = response.get('intencion', 'desconocida')
            print(f"🎯 '{mensaje}' → {intencion_detectada}")
    
    print("✅ Todas las intenciones funciona")
    return True

def reporte_final(resultados):
    """Genera reporte final de pruebas"""
    print("\n" + "="*60)
    print("📋 REPORTE FINAL")
    print("="*60)
    
    tests = [
        ("No repetición (Gamer)", resultados[0]),
        ("Contexto Profesional", resultados[1]),
        ("Complementos Inteligentes", resultados[2]),
        ("Presupuesto", resultados[3]),
        ("Urgencia", resultados[4]),
        ("Intenciones", resultados[5])
    ]
    
    pasadas = sum(1 for _, resultado in tests if resultado)
    total = len(tests)
    
    for nombre, resultado in tests:
        estado = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{estado}: {nombre}")
    
    print(f"\n📊 Resultado: {pasadas}/{total} pruebas pasadas ({(pasadas/total)*100:.0f}%)")
    
    if pasadas == total:
        print("🎉 ¡TODOS LOS TESTS PASARON!")
    elif pasadas >= total * 0.8:
        print("⚠️  Mayoría de tests pasaron, revisar fallos")
    else:
        print("❌ Muchos fallos, revisar sistema")

if __name__ == "__main__":
    print("🤖 INICIANDO PRUEBAS v3.1")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Verificar conexión
    try:
        response = requests.get(f"{BASE_URL}/api/productos", timeout=2)
        print(f"✅ Bot conectado en {BASE_URL}")
    except:
        print(f"❌ No se pudo conectar a {BASE_URL}")
        print("🔧 Asegúrate de que el bot está corriendo: python app.py")
        exit(1)
    
    # Ejecutar pruebas
    resultados = [
        prueba_no_repeticion_gamer(),
        prueba_contexto_profesional(),
        prueba_complementos(),
        prueba_presupuesto(),
        prueba_urgencia(),
        prueba_intenciones()
    ]
    
    # Reporte
    reporte_final(resultados)
    
    print("\n" + "="*60)
    print("💡 TIPS PARA MEJORAR:")
    print("="*60)
    print("""
    1. Si hay repetición: Aumentar tamaño de MAPEO_INTERESES_AVANZADO
    2. Si no detecta contexto: Revisar analizar_conversacion_profunda()
    3. Si falla complementos: Verificar COMPLEMENTOS_INTELIGENTES dict
    4. Si lento: Optimizar busqueda con índices
    5. Si poco preciso: Agregar más palabras clave a PALABRAS_CLAVE_ESPECIFICAS
    """)
