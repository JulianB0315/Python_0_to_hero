"""
Bot Inteligente con NLP avanzado
Responde preguntas complejas usando transformers y spacy
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Tuple
from pathlib import Path

try:
    import spacy
    from transformers import pipeline
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    DEPENDENCIES_AVAILABLE = False
    print("⚠️  Algunas dependencias no están instaladas.")
    print("Ejecuta: pip install -r requirements.txt")


class BotInteligente:
    """Bot que puede responder preguntas complejas con NLP"""
    
    def __init__(self):
        self.modelo_cargado = False
        self.nlp = None
        self.qa_pipeline = None
        self.conversation_history: List[Dict] = []
        self.knowledge_base: Dict[str, str] = {}
        
        # Cargar modelos disponibles
        self._cargar_modelos()
        
    def _cargar_modelos(self):
        """Carga los modelos de NLP disponibles"""
        print("🤖 Inicializando bot inteligente...\n")
        
        # Intentar cargar spacy
        try:
            self.nlp = spacy.load("en_core_web_sm")
            print("✅ Modelo spacy cargado correctamente")
            self.modelo_cargado = True
        except OSError:
            print("⚠️  Modelo spacy no encontrado. Instálalo con:")
            print("   python -m spacy download en_core_web_sm")
        
        # Intentar cargar pipeline de QA (más rápido que cargar BERT completo)
        try:
            print("📚 Cargando pipeline de respuestas...")
            # Usar un modelo más ligero
            self.qa_pipeline = pipeline(
                "question-answering",
                model="deepset/roberta-base-squad2",
                device=-1  # CPU
            )
            print("✅ Pipeline de QA cargado")
        except Exception as e:
            print(f"⚠️  Pipeline de QA no disponible: {e}")
            print("   Se usarán respuestas basadas en palabras clave")
    
    def _analizar_pregunta(self, pregunta: str) -> Dict:
        """Analiza la pregunta usando NLP"""
        analisis = {
            "pregunta_original": pregunta,
            "entidades": [],
            "palabras_clave": [],
            "tipo_pregunta": self._detectar_tipo_pregunta(pregunta)
        }
        
        if self.nlp:
            try:
                doc = self.nlp(pregunta)
                # Extraer entidades
                analisis["entidades"] = [(ent.text, ent.label_) for ent in doc.ents]
                # Extraer palabras clave (sustantivos y verbos)
                analisis["palabras_clave"] = [
                    token.text for token in doc 
                    if token.pos_ in ["NOUN", "VERB", "PROPN"]
                ]
            except Exception as e:
                print(f"Error en análisis: {e}")
        
        return analisis
    
    def _detectar_tipo_pregunta(self, pregunta: str) -> str:
        """Detecta el tipo de pregunta"""
        pregunta_lower = pregunta.lower()
        
        tipos = {
            "que": ["qué", "what"],
            "quien": ["quién", "who"],
            "donde": ["dónde", "donde", "where"],
            "cuando": ["cuándo", "cuando", "when"],
            "como": ["cómo", "como", "how"],
            "por_que": ["por qué", "porqué", "why"],
            "cuanto": ["cuánto", "cuanto", "how many"],
            "si_no": ["es", "está", "puedo", "puede", "hay", "does", "is", "can"]
        }
        
        for tipo, palabras in tipos.items():
            if any(palabra in pregunta_lower for palabra in palabras):
                return tipo
        
        return "general"
    
    def generar_respuesta(self, pregunta: str, contexto: str = "") -> str:
        """Genera una respuesta inteligente a la pregunta"""
        
        # Analizar pregunta
        analisis = self._analizar_pregunta(pregunta)
        
        # Guardar en historial
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "pregunta": pregunta,
            "analisis": analisis
        })
        
        # Estrategia 1: Usar conocimiento base
        respuesta_kb = self._buscar_en_conocimiento(pregunta)
        if respuesta_kb:
            return f"📖 {respuesta_kb}"
        
        # Estrategia 2: Usar pipeline de QA si hay contexto
        if contexto and self.qa_pipeline:
            try:
                resultado = self.qa_pipeline(
                    question=pregunta,
                    context=contexto
                )
                return f"💡 {resultado['answer']}"
            except Exception as e:
                print(f"Error QA: {e}")
        
        # Estrategia 3: Respuesta inteligente basada en análisis
        return self._generar_respuesta_inteligente(pregunta, analisis)
    
    def _buscar_en_conocimiento(self, pregunta: str) -> str:
        """Busca la pregunta en la base de conocimiento"""
        pregunta_lower = pregunta.lower()
        
        for clave, valor in self.knowledge_base.items():
            if clave.lower() in pregunta_lower:
                return valor
        
        return None
    
    def _generar_respuesta_inteligente(self, pregunta: str, analisis: Dict) -> str:
        """Genera respuesta basada en análisis NLP"""
        
        tipo_pregunta = analisis["tipo_pregunta"]
        palabras_clave = analisis["palabras_clave"]
        
        respuestas_base = {
            "que": f"Excelente pregunta sobre {', '.join(palabras_clave) if palabras_clave else 'eso'}. "
                   f"Necesitaría más contexto para darte una respuesta completa.",
            
            "quien": f"Según mi análisis, la pregunta es sobre {', '.join(palabras_clave) if palabras_clave else 'alguien'}. "
                    f"¿Podrías proporcionar más detalles?",
            
            "donde": f"Detecté que preguntas sobre una ubicación relacionada con {', '.join(palabras_clave) if palabras_clave else 'algo'}.",
            
            "cuando": f"Tu pregunta es temporal. Hablas de {', '.join(palabras_clave) if palabras_clave else 'un evento'} "
                     f"que requiere información sobre fechas.",
            
            "como": f"Preguntas 'cómo' sobre {', '.join(palabras_clave) if palabras_clave else 'algo'}. "
                   f"Me gustaría ayudarte con los pasos o proceso.",
            
            "por_que": f"Buscas una razón sobre {', '.join(palabras_clave) if palabras_clave else 'algo'}}. "
                      f"Es una excelente pregunta analítica.",
            
            "cuanto": f"Preguntas sobre cantidad o medida de {', '.join(palabras_clave) if palabras_clave else 'algo'}}.",
            
            "si_no": f"Es una pregunta de sí/no sobre {', '.join(palabras_clave) if palabras_clave else 'algo'}}.",
            
            "general": f"🤔 Pregunta interesante. Entiendo que hablas sobre {', '.join(palabras_clave) if palabras_clave else 'algo'}}. "
                      f"¿Podrías ser más específico?"
        }
        
        if analisis["entidades"]:
            entidades_texto = ", ".join([f"{ent} ({etiqueta})" for ent, etiqueta in analisis["entidades"]])
            respuesta = respuestas_base.get(tipo_pregunta, respuestas_base["general"])
            return f"{respuesta}\n\n📌 Detecté estas entidades: {entidades_texto}"
        
        return respuestas_base.get(tipo_pregunta, respuestas_base["general"])
    
    def agregar_conocimiento(self, pregunta: str, respuesta: str):
        """Agrega un par pregunta-respuesta a la base de conocimiento"""
        self.knowledge_base[pregunta.lower()] = respuesta
        print(f"✅ Conocimiento agregado: '{pregunta}' -> '{respuesta}'")
    
    def cargar_conocimiento_json(self, archivo: str):
        """Carga base de conocimiento desde JSON"""
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                self.knowledge_base.update(json.load(f))
            print(f"✅ Base de conocimiento cargada desde {archivo}")
        except FileNotFoundError:
            print(f"⚠️  Archivo {archivo} no encontrado")
    
    def guardar_conocimiento_json(self, archivo: str):
        """Guarda base de conocimiento en JSON"""
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_base, f, ensure_ascii=False, indent=2)
        print(f"✅ Base de conocimiento guardada en {archivo}")
    
    def mostrar_historial(self):
        """Muestra el historial de conversación"""
        if not self.conversation_history:
            print("📭 No hay historial aún")
            return
        
        print("\n📜 HISTORIAL DE CONVERSACIÓN:")
        print("=" * 60)
        for i, entrada in enumerate(self.conversation_history, 1):
            print(f"\n{i}. [{entrada['timestamp']}]")
            print(f"   Pregunta: {entrada['pregunta']}")
            print(f"   Tipo: {entrada['analisis']['tipo_pregunta']}")
            if entrada['analisis']['palabras_clave']:
                print(f"   Palabras clave: {', '.join(entrada['analisis']['palabras_clave'])}")
        print("\n" + "=" * 60)


def main():
    """Función principal - interfaz conversacional"""
    bot = BotInteligente()
    
    print("\n" + "=" * 60)
    print("🤖 BOT INTELIGENTE - RESPUESTAS COMPLEJAS")
    print("=" * 60)
    print("\nComandos disponibles:")
    print("  - Escribe tu pregunta normalmente")
    print("  - 'aprender' para agregar conocimiento")
    print("  - 'historial' para ver conversaciones")
    print("  - 'salir' para terminar")
    print("=" * 60 + "\n")
    
    # Agregar conocimiento inicial
    bot.agregar_conocimiento("hola", "¡Hola! Soy un bot inteligente. ¿En qué puedo ayudarte?")
    bot.agregar_conocimiento("python", "Python es un lenguaje de programación versátil usado en IA, web, análisis de datos y más")
    bot.agregar_conocimiento("inteligencia artificial", "IA es la simulación de procesos de inteligencia usando máquinas")
    
    while True:
        try:
            entrada = input("\n👤 Tú: ").strip()
            
            if not entrada:
                continue
            
            if entrada.lower() == "salir":
                print("\n👋 ¡Hasta luego!")
                break
            
            elif entrada.lower() == "historial":
                bot.mostrar_historial()
            
            elif entrada.lower() == "aprender":
                pregunta_nueva = input("Pregunta a agregar: ").strip()
                respuesta_nueva = input("Respuesta: ").strip()
                if pregunta_nueva and respuesta_nueva:
                    bot.agregar_conocimiento(pregunta_nueva, respuesta_nueva)
            
            else:
                respuesta = bot.generar_respuesta(entrada)
                print(f"\n🤖 Bot: {respuesta}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Conversación interrumpida. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
