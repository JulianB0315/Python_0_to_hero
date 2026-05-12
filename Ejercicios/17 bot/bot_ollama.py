"""
Bot con Ollama - Respuestas Inteligentes Avanzadas
Requiere Ollama ejecutándose localmente: ollama serve
Soporta múltiples modelos con contexto completo
"""

import requests
import json
import time
from typing import List, Dict, Optional
from pathlib import Path
from datetime import datetime


class BotOllama:
    """Bot que usa Ollama para respuestas más inteligentes"""
    
    def __init__(self, model: str = "mistral", base_url: str = "http://localhost:11434"):
        """
        Inicializa el bot con Ollama
        
        Args:
            model: Modelo a usar (mistral, llama2, neural-chat, etc.)
            base_url: URL de Ollama
        """
        self.base_url = base_url
        self.model = model
        self.conversation_history: List[Dict] = []
        self.is_available = self._check_ollama()
        self.system_prompt = self._crear_system_prompt()
        self.max_history = 10  # Mantener últimas 10 conversaciones
        self.temperature = 0.7
        self.top_p = 0.9
        self.top_k = 40
        
        if self.is_available:
            print(f"✅ Conectado a Ollama con modelo: {model}")
            print(f"   Temperatura: {self.temperature}")
            print(f"   Top P: {self.top_p}")
        else:
            print("⚠️  Ollama no está disponible")
            print("   Instala Ollama desde: https://ollama.ai")
            print("   Y ejecuta: ollama serve")
    
    def _check_ollama(self) -> bool:
        """Verifica si Ollama está disponible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def generar_respuesta(self, pregunta: str) -> str:
        """Genera respuesta usando Ollama"""
        
        if not self.is_available:
            return "❌ Ollama no está disponible. Por favor inicia Ollama primero."
        
        # Guardar contexto de conversación
        contexto = ""
        if self.conversation_history:
            contexto = "Contexto previo de la conversación:\n"
            for msg in self.conversation_history[-3:]:  # Últimos 3 mensajes
                contexto += f"- {msg['pregunta']}\n"
        
        prompt = f"""{contexto}
Responde de manera clara, útil y concisa.
Pregunta: {pregunta}
Respuesta:"""
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7
                },
                timeout=60
            )
            
            if response.status_code == 200:
                resultado = response.json()
                respuesta = resultado.get("response", "No se pudo generar respuesta")
                
                # Guardar en historial
                self.conversation_history.append({
                    "pregunta": pregunta,
                    "respuesta": respuesta
                })
                
                return respuesta.strip()
            else:
                return f"❌ Error: {response.status_code}"
        
        except requests.exceptions.Timeout:
            return "⏱️  La respuesta tardó demasiado. Intenta de nuevo."
        except Exception as e:
            return f"❌ Error: {e}"
    
    def generar_respuesta_streaming(self, pregunta: str):
        """Genera respuesta con streaming (muestra en tiempo real)"""
        
        if not self.is_available:
            print("❌ Ollama no está disponible")
            return
        
        prompt = f"Responde claramente: {pregunta}"
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": True,
                    "temperature": 0.7
                },
                stream=True,
                timeout=120
            )
            
            respuesta_completa = ""
            print("\n🤖 Bot: ", end="", flush=True)
            
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    texto = data.get("response", "")
                    print(texto, end="", flush=True)
                    respuesta_completa += texto
            
            print()  # Nueva línea
            
            # Guardar en historial
            self.conversation_history.append({
                "pregunta": pregunta,
                "respuesta": respuesta_completa
            })
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    def modelos_disponibles(self) -> List[str]:
        """Lista modelos disponibles en Ollama"""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                data = response.json()
                return [model["name"] for model in data.get("models", [])]
        except:
            pass
        return []
    
    def cambiar_modelo(self, modelo: str):
        """Cambia el modelo a usar"""
        modelos = self.modelos_disponibles()
        
        if modelo in modelos or any(modelo in m for m in modelos):
            self.model = modelo
            print(f"✅ Modelo cambiado a: {modelo}")
        else:
            print(f"❌ Modelo '{modelo}' no disponible")
            print(f"Modelos disponibles: {', '.join(modelos)}")


def main():
    """Interfaz principal del bot Ollama"""
    
    print("\n" + "=" * 60)
    print("🤖 BOT OLLAMA - RESPUESTAS AVANZADAS")
    print("=" * 60)
    
    bot = BotOllama(model="mistral")
    
    if not bot.is_available:
        print("\n⚠️  IMPORTANTE: Ollama no está corriendo")
        print("\nPasos para usar este bot:")
        print("1. Instala Ollama desde https://ollama.ai")
        print("2. Abre PowerShell y ejecuta:")
        print("   & \"C:\\Users\\julia\\AppData\\Local\\Programs\\Ollama\\ollama.exe\" serve")
        print("3. En otra terminal, ejecuta este script")
        return
    
    print("\nComandos:")
    print("  - Escribe tu pregunta normalmente")
    print("  - 'modelos' para ver modelos disponibles")
    print("  - 'cambiar' para cambiar modelo")
    print("  - 'streaming' para habilitar respuestas en vivo")
    print("  - 'salir' para terminar")
    print("=" * 60 + "\n")
    
    streaming_mode = False
    
    while True:
        try:
            entrada = input("\n👤 Tú: ").strip()
            
            if not entrada:
                continue
            
            if entrada.lower() == "salir":
                print("\n👋 ¡Hasta luego!")
                break
            
            elif entrada.lower() == "modelos":
                modelos = bot.modelos_disponibles()
                if modelos:
                    print(f"\n📚 Modelos disponibles:")
                    for modelo in modelos:
                        print(f"   - {modelo}")
                else:
                    print("❌ No hay modelos disponibles")
            
            elif entrada.lower() == "cambiar":
                nuevo_modelo = input("Nuevo modelo: ").strip()
                bot.cambiar_modelo(nuevo_modelo)
            
            elif entrada.lower() == "streaming":
                streaming_mode = not streaming_mode
                print(f"🔄 Streaming: {'ACTIVADO' if streaming_mode else 'DESACTIVADO'}")
            
            else:
                if streaming_mode:
                    bot.generar_respuesta_streaming(entrada)
                else:
                    respuesta = bot.generar_respuesta(entrada)
                    print(f"\n🤖 Bot: {respuesta}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Conversación interrumpida")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
