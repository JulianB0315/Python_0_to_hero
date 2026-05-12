#!/usr/bin/env python3
"""
📝 EJEMPLO COMPLETO DE CONVERSACIÓN
Muestra cómo el bot es inteligente para recomendar productos
Ejecuta: python ejemplo_conversacion.py
"""

import json
from datetime import datetime

# Cargar datos
with open('productos.json', 'r', encoding='utf-8') as f:
    PRODUCTOS = json.load(f)['productos']

print("="*70)
print("🤖 EJEMPLO DE CONVERSACIÓN INTELIGENTE - TECHSTORE BOT v3")
print("="*70)
print()

# Ejemplo 1: Usuario Gamer
print("📌 ESCENARIO 1: USUARIO GAMER")
print("-"*70)
print("""
TÚ:    Hola, soy gamer profesional y necesito mejorar mi setup
BOT:   ¡Hola! Veo que te interesa: gaming 🚀
       
       💡 Productos que podrían interesarte:
       • Teclado Mecánico Corsair - $189.99
         Teclado mecánico RGB para gaming y escritura
       • Mouse Logitech MX Master - $99.99
         Ratón inalámbrico profesional de precisión

TÚ:    ¿Qué diferencia hay entre esos dos?
BOT:   El Teclado Corsair es para escribir rápido con switches MX Red
       El Mouse Logitech es de precisión para gaming competitivo 😊
       
       ¿Quieres ambos? Te combinarían perfecto 🎮

TÚ:    Dale, agrégame el teclado
BOT:   ✅ ¡Perfecto! Agregué 'Teclado Mecánico Corsair' ($189.99)
       
       💡 Productos que combinan bien:
       • Mouse Logitech MX Master ($99.99)
       
       📊 Total actual: $189.99

TÚ:    y el mouse también
BOT:   ✅ ¡Excelente! Agregué 'Mouse Logitech MX Master' ($99.99)
       
       📊 Total actual: $289.98
       
       ¿Necesitas algo más para tu setup? 😊
""")
print()

# Ejemplo 2: Usuario profesional
print("📌 ESCENARIO 2: USUARIO PROFESIONAL (TRABAJO REMOTO)")
print("-"*70)
print("""
TÚ:    Necesito mejorar mi productividad en el trabajo remoto
BOT:   ¡Entiendo! ¿Qué tipo de trabajo haces? 🤔

TÚ:    Edito videos y diseño gráfico desde casa
BOT:   Ah, necesitas potencia y pantalla. Veo: fotografía, potencia
       
       💡 Te recomiendo:
       • Laptop ASUS VivoBook - $799.99
         Intel i7, 16GB RAM, SSD 512GB
       • Monitor LG UltraWide - $449.99
         34\", 3440x1440, 144Hz para multitarea

TÚ:    El monitor suena bien
BOT:   ✅ Agregué 'Monitor LG UltraWide' ($449.99)
       
       💡 Para ir con el monitor, necesitas:
       • Mouse Logitech MX Master ($99.99) - perfecto para diseño
       • Laptop ASUS VivoBook ($799.99) - potencia para edición
       
       📊 Total: $449.99

TÚ:    Dale todo de una
BOT:   ✅ Agregué 'Laptop ASUS VivoBook' ($799.99)
       ✅ Agregué 'Mouse Logitech MX Master' ($99.99)
       
       💡 Úsalo así: Monitor + Laptop + Mouse = setup profesional 💼
       
       📊 Total actual: $1.349.97
""")
print()

# Ejemplo 3: Usuario viajero
print("📌 ESCENARIO 3: USUARIO VIAJERO")
print("-"*70)
print("""
TÚ:    Viajo constantemente y necesito algo ligero y compacto
BOT:   ¡Perfecto! Veo: viaje, portátil
       
       💡 Te recomiendo:
       • Laptop ASUS VivoBook - $799.99
         Ultradelgada, perfecta para viajar
       • Powerbank Anker - $49.99
         25000mAh, carga rápida 100W

TÚ:    ¿Cuánto pesa el laptop?
BOT:   El ASUS VivoBook es ultradelgado de 1.8kg aproximadamente
       Perfecto para viajar todo el día ✈️

TÚ:    Dale, agrégame el powerbank al menos
BOT:   ✅ Agregué 'Powerbank Anker' ($49.99)
       
       💡 Si después quieres el laptop, te deja sin carga cero 🔋
       
       📊 Total: $49.99

TÚ:    Bueno, agregame el laptop también entonces
BOT:   ✅ ¡Excelente opción! Agregué 'Laptop ASUS VivoBook' ($799.99)
       
       Tienes el combo perfecto para viajar:
       • Laptop ultradelgada + Powerbank = viajes sin preocupaciones ✈️
       
       📊 Total actual: $849.98
""")
print()

# Ejemplo 4: Usuario que no sabe qué quiere
print("📌 ESCENARIO 4: USUARIO SIN DECISIÓN")
print("-"*70)
print("""
TÚ:    Hola, no sé qué comprar pero me encanta la tecnología
BOT:   ¡Bienvenido! 👋 Me encanta tu entusiasmo 😊
       
       Cuéntame un poco:
       ¿Eres gamer? ¿Trabajas con tech? ¿Viajas mucho?
       ¿Haces videos/fotos? ¿Qué tipo de tech te llama?

TÚ:    Hmm, un poco de todo. Sobre todo me interesa el audio
BOT:   ¡Excelente! Veo: audio
       
       💡 Te recomiendo nuestros mejores auriculares:
       • Samsung Galaxy Buds - $149.99
         ANC, Batería 6h, Carga inalámbrica
       • Sony WH-1000XM5 - $349.99
         ANC líder, 30h batería, Sonido premium

TÚ:    ¿Cuál es mejor?
BOT:   Depende tu uso:
       - Galaxy Buds: Para portabilidad (viajes)
       - Sony: Para usar todo el día en oficina/casa
       
       ¿Cuál es tu caso? 🎧

TÚ:    Viajo mucho
BOT:   Perfecto, entonces Galaxy Buds. Agrégame
       
       ✅ Agregué 'Samsung Galaxy Buds' ($149.99)
       
       💡 Para viajes también te iría bien:
       • Powerbank Anker ($49.99) - para cargar en vuelos
       
       📊 Total: $149.99
""")

print()
print("="*70)
print("✨ CONCLUSIÓN")
print("="*70)
print("""
El bot ahora:
✅ Entiende qué tipo de usuario eres
✅ Recomienda productos relevantes sin presionar
✅ Sugiere complementos inteligentes
✅ Adapta respuestas según contexto
✅ Aprende de la conversación
✅ Es como un vendedor profesional pero amable

Todo de forma NATURAL, sin que parezca forzado 🤖💬
""")
print()
print("📁 Archivos importantes:")
print("  - app.py: Backend con lógica de recomendación")
print("  - SISTEMA_RECOMENDACION.md: Documentación completa")
print("  - productos.json: Base de datos")
print()
