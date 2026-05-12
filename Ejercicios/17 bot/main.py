"""
Demo simple del bot - Para probar rápidamente
Sin dependencias complejas
"""

def demo_bot_simple():
    """Demo básica sin necesidad de instalar todo"""
    
    print("\n" + "=" * 60)
    print("🤖 DEMO BOT SIMPLE - PRUEBA RÁPIDA")
    print("=" * 60 + "\n")
    
    # Base de conocimiento simple
    conocimiento = {
        "hola": "¡Hola! ¿En qué puedo ayudarte?",
        "python": "Python es un lenguaje de programación versátil. Se usa en AI, web, datos y más.",
        "qué es ia": "IA (Inteligencia Artificial) es la simulación de inteligencia usando máquinas.",
        "ayuda": "Escribe cualquier pregunta. Algunos temas: python, ia, bot, help",
        "quién eres": "Soy un bot inteligente creado en Python para ayudarte con respuestas complejas.",
        "bot": "Yo soy un bot inteligente. ¿Quieres aprender a crear bots?",
        "help": "Escribe: python, ia, quién eres, ayuda, o cualquier pregunta",
    }
    
    print("Preguntas disponibles: python, ia, quién eres, ayuda, bot, help")
    print("Escribe 'salir' para terminar\n")
    
    while True:
        pregunta = input("👤 Tú: ").strip().lower()
        
        if not pregunta:
            continue
        
        if pregunta == "salir":
            print("\n👋 ¡Hasta luego!")
            break
        
        # Buscar respuesta
        respuesta = None
        for clave, valor in conocimiento.items():
            if clave in pregunta:
                respuesta = valor
                break
        
        if not respuesta:
            # Generar respuesta inteligente
            if "?" in pregunta:
                respuesta = f"Es una pregunta interesante sobre '{pregunta}'. Necesito más contexto para responderte mejor."
            else:
                respuesta = f"Interesante pregunta. ¿Podrías ser más específico?"
        
        print(f"\n🤖 Bot: {respuesta}\n")


def menu_principal():
    """Menú para elegir qué hacer"""
    
    print("\n" + "=" * 60)
    print("🤖 BOT INTELIGENTE - MENU PRINCIPAL")
    print("=" * 60)
    print("\nOpciones:")
    print("1. Demo simple (prueba rápida, sin instalación)")
    print("2. Iniciar bot_inteligente.py (requiere: pip install -r requirements.txt)")
    print("3. Iniciar bot_ollama.py (requiere: Ollama instalado)")
    print("4. Ver guía de instalación")
    print("5. Salir")
    print("=" * 60)
    
    while True:
        opcion = input("\nElige opción (1-5): ").strip()
        
        if opcion == "1":
            demo_bot_simple()
            break
        
        elif opcion == "2":
            print("\n📝 Ejecutando: python bot_inteligente.py")
            print("\nPrimero instala dependencias:")
            print("  pip install -r requirements.txt")
            print("  python -m spacy download en_core_web_sm")
            print("\nLuego ejecuta:")
            print("  python bot_inteligente.py")
            break
        
        elif opcion == "3":
            print("\n📝 Ejecutando: python bot_ollama.py")
            print("\n⚠️  Primero debes tener Ollama corriendo:")
            print("  1. Ve a https://ollama.ai")
            print("  2. Descarga e instala Ollama")
            print("  3. Ejecuta en terminal: ollama serve")
            print("  4. En otra terminal: python bot_ollama.py")
            break
        
        elif opcion == "4":
            print("\n📖 GUÍA DE INSTALACIÓN\n")
            print("1️⃣  BOT INTELIGENTE (RECOMENDADO)")
            print("-" * 40)
            print("pip install -r requirements.txt")
            print("python -m spacy download en_core_web_sm")
            print("python bot_inteligente.py")
            print("\n2️⃣  BOT OLLAMA (AVANZADO)")
            print("-" * 40)
            print("Paso 1: Instala Ollama")
            print("  - Ve a https://ollama.ai")
            print("  - Descarga e instala")
            print("\nPaso 2: Inicia Ollama")
            print("  - PowerShell: ollama serve")
            print("  - Espera: 'listening on 127.0.0.1:11434'")
            print("\nPaso 3: Ejecuta el bot")
            print("  - pip install -r requirements.txt")
            print("  - python bot_ollama.py")
            break
        
        elif opcion == "5":
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    import sys
    
    # Si se pasa argumento "demo", ejecutar demo directamente
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_bot_simple()
    else:
        menu_principal()
