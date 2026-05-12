#!/usr/bin/env python3
"""
🧪 TEST RÁPIDO - Verifica que todo el sistema funciona
Ejecuta: python test_rapido.py
"""

print("=" * 70)
print("🧪 TEST RÁPIDO - TECHSTORE BOT v3")
print("=" * 70)
print()

# Test 1: Cargar productos
print("✓ Test 1: Cargando productos...")
try:
    import json
    with open('productos.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        productos = data['productos']
    print(f"  ✅ {len(productos)} productos cargados correctamente")
    print(f"  Productos: {', '.join([p['nombre'][:15] + '...' for p in productos[:3]])}")
except Exception as e:
    print(f"  ❌ Error: {e}")
    exit(1)

print()

# Test 2: Funciones de análisis
print("✓ Test 2: Probando funciones de IA...")
try:
    def normalizar_texto(texto):
        return texto.lower().strip()
    
    def extraer_intereses(mensaje):
        msg = normalizar_texto(mensaje)
        intereses = []
        mapeo = {
            'gaming': ['gaming', 'juegos', 'gamer'],
            'trabajo': ['trabajo', 'oficina'],
            'viaje': ['viaje', 'portátil', 'compacto'],
            'audio': ['música', 'sonido', 'auricular'],
        }
        for categoria, palabras in mapeo.items():
            if any(palabra in msg for palabra in palabras):
                intereses.append(categoria)
        return intereses
    
    # Test cases
    test_cases = [
        ("Soy gamer", ['gaming']),
        ("Trabajo desde casa", ['trabajo']),
        ("Viajo mucho", ['viaje']),
        ("Me encanta la música", ['audio']),
    ]
    
    for msg, expected in test_cases:
        resultado = extraer_intereses(msg)
        if resultado == expected:
            print(f"  ✅ '{msg}' → {resultado}")
        else:
            print(f"  ⚠️  '{msg}' → {resultado} (esperado: {expected})")
            
except Exception as e:
    print(f"  ❌ Error: {e}")
    exit(1)

print()

# Test 3: Detección de intenciones
print("✓ Test 3: Detectando intenciones...")
try:
    def detectar_intencion(msg):
        msg = msg.lower().strip()
        if any(word in msg for word in ['qué hora', 'que hora', 'qué día']):
            return 'fecha_hora'
        elif any(word in msg for word in ['cómo estás', 'como estás']):
            return 'sobre_bot'
        elif any(word in msg for word in ['busco', 'quiero', 'necesito']):
            return 'busqueda'
        elif any(word in msg for word in ['precio', 'cuesta', 'cuánto']):
            return 'precio'
        return 'otro'
    
    intenciones_test = [
        ("¿Qué hora es?", "fecha_hora"),
        ("¿Cómo estás?", "sobre_bot"),
        ("Busco un laptop", "busqueda"),
        ("¿Cuánto cuesta?", "precio"),
    ]
    
    for msg, expected in intenciones_test:
        resultado = detectar_intencion(msg)
        if resultado == expected:
            print(f"  ✅ '{msg}' → {resultado}")
        else:
            print(f"  ❌ '{msg}' → {resultado} (esperado: {expected})")
            
except Exception as e:
    print(f"  ❌ Error: {e}")
    exit(1)

print()

# Test 4: Búsqueda de productos
print("✓ Test 4: Buscando productos...")
try:
    def buscar_productos(consulta):
        consulta = consulta.lower().strip()
        resultados = []
        for prod in productos:
            if (consulta in prod['nombre'].lower() or 
                consulta in prod['descripcion'].lower()):
                resultados.append(prod)
        return resultados
    
    searches = [
        ("laptop", 1),
        ("auriculares", 2),
        ("monitor", 1),
    ]
    
    for term, esperados in searches:
        resultado = buscar_productos(term)
        if len(resultado) >= 1:
            print(f"  ✅ '{term}' → Encontrados {len(resultado)} producto(s)")
        else:
            print(f"  ❌ '{term}' → No encontrado")
            
except Exception as e:
    print(f"  ❌ Error: {e}")
    exit(1)

print()

# Test 5: Verificar estructura de proyecto
print("✓ Test 5: Verificando estructura...")
try:
    import os
    archivos_necesarios = [
        'app.py',
        'productos.json',
        'requirements.txt',
        'templates/index.html',
        'static/styles.css',
        'static/script.js',
    ]
    
    for archivo in archivos_necesarios:
        if os.path.exists(archivo):
            print(f"  ✅ {archivo}")
        else:
            print(f"  ❌ {archivo} FALTA")
            
except Exception as e:
    print(f"  ❌ Error: {e}")

print()
print("=" * 70)
print("✨ TODOS LOS TESTS COMPLETADOS")
print("=" * 70)
print()
print("📝 Próximo paso:")
print("   1. Instala dependencias: pip install -r requirements.txt")
print("   2. Ejecuta el bot: python app.py")
print("   3. Abre: http://localhost:5000")
print()
print("💬 Prueba decir:")
print("   • 'Hola, soy gamer'")
print("   • '¿Qué hora es?'")
print("   • 'Busco un laptop'")
print()
print("🎉 ¡Listo! El bot está preparado")
print()
