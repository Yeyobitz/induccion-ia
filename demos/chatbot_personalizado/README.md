# Demo 1: Chatbot Personalizado

¡Bienvenido al demo del Chatbot Personalizado!

**Concepto:**
Este proyecto es un esqueleto de un chatbot muy simple. La idea es que lo personalices y expandas utilizando IA para que pueda mantener conversaciones más interesantes y útiles.

**Estado Actual:**
El chatbot actualmente solo puede responder a un saludo básico. Si miras el archivo `chatbot.py` (que tendrás que crear), verás que la lógica es muy limitada.

```python
# chatbot.py (Ejemplo inicial - ¡puedes pedirle a la IA que lo genere!)
def obtener_respuesta(mensaje_usuario):
    mensaje_usuario = mensaje_usuario.lower()
    if "hola" in mensaje_usuario or "saludos" in mensaje_usuario:
        return "¡Hola! ¿Cómo puedo ayudarte hoy?"
    else:
        return "Lo siento, no entendí eso. ¿Podrías repetirlo?"

# Bucle principal para interactuar con el chatbot (pídele a la IA que lo mejore)
# while True:
#     entrada = input("Tú: ")
#     if entrada.lower() == "salir":
#         print("Chatbot: Adiós!")
#         break
#     respuesta = obtener_respuesta(entrada)
#     print(f"Chatbot: {respuesta}")
```

**Tu Misión (con ayuda de la IA):**

1.  **Genera el archivo `chatbot.py` inicial:** Pídele a tu asistente de IA: "Genera un archivo Python llamado `chatbot.py` con una función `obtener_respuesta(mensaje_usuario)` que devuelva un saludo si el mensaje contiene 'hola' y un mensaje de 'no entendí' en caso contrario. También incluye un bucle simple para interactuar con el chatbot desde la consola."
2.  **Añade más intenciones:**
    *   Dile a la IA: "Modifica `chatbot.py` para que el chatbot pueda responder preguntas sobre el clima. Por ejemplo, si le pregunto '¿cómo está el clima?', debería dar una respuesta genérica sobre el clima."
    *   Piensa en otras preguntas o temas que te gustaría que tu chatbot maneje (chistes, datos curiosos, etc.) y pídele a la IA que te ayude a implementar esas nuevas "intenciones" y sus respuestas.
3.  **Mejora la comprensión:**
    *   El chatbot actual usa una simple búsqueda de palabras clave. Pregúntale a la IA: "¿Cómo puedo hacer que el chatbot entienda variaciones de la misma pregunta? Por ejemplo, que 'dime el clima' y 'pronóstico del tiempo' activen la misma respuesta." (Podría sugerir usar expresiones regulares o incluso introducir conceptos de NLP más avanzados si te sientes aventurero).
4.  **Personaliza sus respuestas:**
    *   Haz que las respuestas del chatbot sean más variadas. Pídele a la IA: "En `chatbot.py`, cuando el chatbot saluda, quiero que elija aleatoriamente entre 3 saludos diferentes."
5.  **Añade memoria (opcional avanzado):**
    *   Pregúntale a la IA: "¿Cómo podría hacer para que el chatbot recuerde mi nombre después de que se lo digo?"
6.  **Potencia con un LLM (Desafío Avanzado):**
    *   Para llevar tu chatbot al siguiente nivel, investiga cómo integrar una API de un Modelo de Lenguaje Grande (LLM) como los de OpenAI, Gemini, Claude, etc. Pídele a tu IA: "Muéstrame cómo puedo conectar mi chatbot de Python a una API de LLM para generar respuestas más naturales y complejas." Esto podría reemplazar o complementar tu lógica de `obtener_respuesta`.
    *   Explora cómo enviar el historial de la conversación al LLM para que tenga más contexto.

**Objetivo:**
Experimenta cómo la IA puede ayudarte a escribir código, generar ideas para la lógica de conversación y mejorar la funcionalidad de una aplicación simple. ¡Diviértete creando tu propio chatbot! 