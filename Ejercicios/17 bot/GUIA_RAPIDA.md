# 🚀 Guía Rápida - Bot Inteligente

## ¿Cuál usar?

### Quiero empezar YA → **bot_inteligente.py**
- Instalación fácil
- Funciona inmediatamente
- Buenas respuestas

### Quiero respuestas profesionales → **bot_ollama.py**
- Más inteligente
- Mejor comprensión del contexto
- Requiere configuración extra

---

## ⚡ Inicio Rápido

### Opción 1: Bot Inteligente (RECOMENDADO)

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Descargar modelo
python -m spacy download en_core_web_sm

# 3. ¡Ejecutar!
python bot_inteligente.py
```

### Opción 2: Bot Ollama (Más avanzado)

```bash
# 1. Instalar Ollama
# Ve a https://ollama.ai y descarga

# 2. Ejecutar Ollama en terminal
ollama serve

# 3. En otra terminal
pip install -r requirements.txt
python bot_ollama.py
```

---

## 💬 Ejemplos de uso

### Bot Inteligente

```
👤 Tú: ¿Qué es machine learning?
🤖 Bot: 💡 Es una rama de la IA que permite a máquinas aprender...

👤 Tú: aprender
Pregunta: ¿Quién eres?
Respuesta: Soy tu asistente Python

👤 Tú: ¿Quién eres?
🤖 Bot: 📖 Soy tu asistente Python

👤 Tú: historial
📜 HISTORIAL DE CONVERSACIÓN...
```

### Bot Ollama

```
👤 Tú: Explícame redes neuronales
🤖 Bot: Las redes neuronales son modelos computacionales 
        inspirados en el cerebro humano...

👤 Tú: streaming
🔄 Streaming: ACTIVADO

👤 Tú: ¿Cómo entreno un modelo?
🤖 Bot: [Respuesta en vivo, palabra por palabra...]
```

---

## 📊 Tabla Comparativa Rápida

| Criterio | bot_inteligente | bot_ollama |
|---|---|---|
| Instalación | ✅ Fácil | 🔴 Compleja |
| Tiempo inicio | ⚡ Inmediato | ⏱️ 30-60s |
| Calidad respuesta | 🟡 Buena | 🟢 Excelente |
| Contexto | 📄 Limitado | 📚 Completo |
| Privacidad | 🔒 Total | 🔒 Total |

---

## ❌ Si algo falla

**"ModuleNotFoundError: No module named 'spacy'"**
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

**"Ollama not available"**
1. Ve a https://ollama.ai y descarga
2. Instala y ejecuta: `ollama serve`
3. Espera a ver: "listening on 127.0.0.1:11434"

**Bot responde muy corto**
- Usa `bot_ollama.py` (responde mejor)
- O agrega conocimiento con `aprender`

---

## 🎮 Comandos Principales

### bot_inteligente.py
| Comando | Uso |
|---|---|
| Pregunta normal | Haz una pregunta cualquiera |
| `aprender` | Enseña al bot |
| `historial` | Ve conversaciones previas |
| `salir` | Termina |

### bot_ollama.py
| Comando | Uso |
|---|---|
| Pregunta normal | Haz una pregunta |
| `modelos` | Ve modelos disponibles |
| `cambiar` | Cambia de modelo |
| `streaming` | Activa respuestas en vivo |
| `salir` | Termina |

---

## 💡 Trucos

### Bot Inteligente
- Guarda preguntas importantes con `aprender`
- Usa `historial` para revisar
- Más específico = mejor respuesta

### Bot Ollama
- Activa `streaming` para ver respuestas en vivo
- Usa contexto previo en preguntas
- Prueba diferentes modelos

---

## 📞 Soporte Rápido

```python
# Si algo explota, copia esto en Python:
import traceback
try:
    # tu código
except Exception as e:
    traceback.print_exc()
    print(f"Error: {e}")
```

---

**¡Listo para empezar!** 🚀
