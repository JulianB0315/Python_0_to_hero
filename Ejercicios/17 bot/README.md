# 🤖 Bot Inteligente - Respuestas Complejas

Este proyecto incluye dos bots diferentes que pueden dar respuestas complejas usando NLP avanzado.

## 📋 Contenido

### 1. **bot_inteligente.py** - Bot con NLP Local
Bot que funciona sin necesidad de conexión a internet usando:
- **spaCy** para análisis de lenguaje natural
- **Transformers** para preguntas y respuestas (QA)
- **Base de conocimiento** personalizable

**Ventajas:**
- ✅ Funciona sin internet
- ✅ Más rápido
- ✅ Privacidad garantizada
- ✅ Bajo uso de recursos

### 2. **bot_ollama.py** - Bot con Ollama
Bot que usa Ollama para respuestas más inteligentes y conversacionales.
- Modelos locales como Mistral, Llama2, Neural-Chat
- Streaming de respuestas (vé la respuesta en tiempo real)
- Contexto de conversación

**Ventajas:**
- ✅ Respuestas más naturales
- ✅ Entiende mejor el contexto
- ✅ Modelos actualizados
- ✅ Streaming en vivo

## 🚀 Instalación

### Requisitos
- Python 3.11+
- pip

### Paso 1: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 2: Descargar modelos de spaCy (si usas bot_inteligente.py)

```bash
python -m spacy download en_core_web_sm
```

### Paso 3 (Opcional): Instalar Ollama (si usas bot_ollama.py)

1. Descarga Ollama desde: https://ollama.ai
2. Instálalo y ejecuta:
```bash
ollama serve
```

3. En otra terminal, descarga un modelo:
```bash
ollama pull mistral
# o
ollama pull llama2
```

## 💻 Uso

### Bot Inteligente (Recomendado para empezar)

```bash
python bot_inteligente.py
```

**Ejemplo de conversación:**
```
👤 Tú: ¿Qué es Python?
🤖 Bot: 📖 Python es un lenguaje de programación versátil usado en IA, web, análisis de datos y más

👤 Tú: ¿Dónde se usa?
🤖 Bot: 💡 Se usa en desarrollo web, ciencia de datos, automatización, inteligencia artificial y más

👤 Tú: aprender
Pregunta a agregar: ¿Cuál es tu nombre?
Respuesta: Soy un bot inteligente creado en Python

👤 Tú: ¿Cuál es tu nombre?
🤖 Bot: 📖 Soy un bot inteligente creado en Python
```

**Comandos:**
- Escribe tu pregunta normalmente
- `aprender` - Agregar nueva pregunta/respuesta a la base de conocimiento
- `historial` - Ver historial de conversaciones
- `salir` - Terminar

### Bot Ollama (Respuestas más avanzadas)

```bash
python bot_ollama.py
```

**Comandos:**
- Escribe tu pregunta normalmente
- `modelos` - Ver modelos disponibles
- `cambiar` - Cambiar modelo
- `streaming` - Activar/desactivar respuestas en vivo
- `salir` - Terminar

## 📊 Comparación

| Característica | bot_inteligente | bot_ollama |
|---|---|---|
| Requiere instalación extra | No | Sí (Ollama) |
| Velocidad | ⚡⚡ Rápido | ⚡ Medio |
| Calidad respuesta | 🟡 Buena | 🟢 Excelente |
| Uso de memoria | 🟢 Bajo | 🔴 Alto |
| Sin internet | ✅ Sí | ✅ Sí |
| Contexto conversación | 🟡 Limitado | 🟢 Completo |

## 🎯 Casos de uso

### Bot Inteligente
- ✅ Búsqueda de información
- ✅ Análisis de preguntas
- ✅ Base de conocimiento personal
- ✅ Clasificación de textos
- ✅ Extracción de entidades

### Bot Ollama
- ✅ Conversaciones naturales
- ✅ Explicaciones detalladas
- ✅ Análisis profundo
- ✅ Creatividad
- ✅ Razonamiento complejo

## 📝 Personalización

### Agregar conocimiento a bot_inteligente.py

En el código, busca la sección en `main()`:

```python
# Agregar conocimiento inicial
bot.agregar_conocimiento("hola", "¡Hola! Soy un bot inteligente...")
bot.agregar_conocimiento("python", "Python es un lenguaje...")
```

O mientras el bot está corriendo, usa el comando `aprender`.

### Cambiar modelo en bot_ollama.py

```bash
python bot_ollama.py
# Luego usa el comando "cambiar" para seleccionar otro modelo
```

Modelos disponibles:
- `mistral` (recomendado, balance)
- `llama2` (especializado)
- `neural-chat` (conversacional)
- `dolphin-mixtral` (más completo)

## ⚙️ Requisitos del Sistema

| Componente | Mínimo | Recomendado |
|---|---|---|
| RAM | 4 GB | 8 GB+ |
| CPU | Dual Core | Quad Core+ |
| Almacenamiento | 2 GB | 10 GB+ |
| Python | 3.9+ | 3.11+ |

## 🐛 Solución de problemas

### Error: "No module named 'spacy'"
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Error: "Ollama not available"
- Descarga Ollama desde https://ollama.ai
- Ejecuta: `ollama serve`
- Espera a que diga "listening on 127.0.0.1:11434"

### Bot muy lento
- Usa `bot_inteligente.py` (más rápido)
- Asigna más RAM
- Cierra otras aplicaciones

### Respuestas cortas o genéricas
- Agrega más conocimiento con `aprender`
- Usa `bot_ollama.py` para respuestas más detalladas
- Sé más específico en tus preguntas

## 📚 Recursos

- [spaCy Documentation](https://spacy.io)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Ollama](https://ollama.ai)
- [Python NLP Guide](https://www.nltk.org)

## 📄 Licencia

Libre para usar y modificar

## 💡 Ideas futuras

- [ ] Integración con APIs (OpenAI, Google, etc.)
- [ ] Aprendizaje de usuario persistente
- [ ] Interfaz gráfica (GUI)
- [ ] Respuestas multiidioma
- [ ] Integración con webhooks
- [ ] Base de datos MongoDB
- [ ] API REST del bot

---

**¡Disfruta tu bot inteligente!** 🚀
