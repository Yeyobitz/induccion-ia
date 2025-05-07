# Demo 3: Traductor de Emoji 🤯🎉

¡Prepárate para hablar el idioma universal del emoji!

**Concepto:**
Este proyecto busca crear una herramienta que pueda traducir texto normal a una secuencia de emojis que representen el significado, y viceversa. ¡Imagina enviar mensajes secretos o simplemente hacer tus chats más divertidos!

**Estado Actual:**
Comenzaremos desde cero. Tu primera tarea será pedirle a la IA que cree la estructura básica.

```python
# traductor_emoji.py (esqueleto inicial que puedes pedir a la IA)

# Ejemplo de un diccionario básico de mapeo (¡la IA puede ayudarte a expandirlo!)
TEXTO_A_EMOJI = {
    "feliz": "😊",
    "triste": "😢",
    "corazón": "❤️",
    "sol": "☀️",
    "comida": "🍕",
    "fiesta": "🎉",
    "dinero": "💰",
    "idea": "💡",
    "fuego": "🔥",
    "ola": "👋"
}

EMOJI_A_TEXTO = {v: k for k, v in TEXTO_A_EMOJI.items()} # Invertir el diccionario

def traducir_a_emoji(texto):
    palabras = texto.lower().split()
    resultado_emoji = []
    for palabra in palabras:
        # Eliminar puntuación simple para mejorar el match
        palabra_limpia = ''.join(filter(str.isalnum, palabra))
        if palabra_limpia in TEXTO_A_EMOJI:
            resultado_emoji.append(TEXTO_A_EMOJI[palabra_limpia])
        # else:
            # Podríamos mantener la palabra original si no hay emoji
            # resultado_emoji.append(palabra) 
    return " ".join(resultado_emoji)

def traducir_a_texto(emojis):
    lista_emojis = emojis.split()
    resultado_texto = []
    for emoji in lista_emojis:
        if emoji in EMOJI_A_TEXTO:
            resultado_texto.append(EMOJI_A_TEXTO[emoji])
        # else:
            # Podríamos mantener el emoji original si no hay texto
            # resultado_texto.append(emoji)
    return " ".join(resultado_texto)

# Ejemplo de uso (pídele a la IA que cree una interfaz de consola)
# texto_original = "Estoy feliz y quiero comida"
# emojis_traducidos = traducir_a_emoji(texto_original)
# print(f"'{texto_original}' -> '{emojis_traducidos}'")

# texto_recuperado = traducir_a_texto(emojis_traducidos)
# print(f"'{emojis_traducidos}' -> '{texto_recuperado}'")
```

**Tu Misión (con ayuda de la IA):**

1.  **Genera el script `traductor_emoji.py`:**
    *   Pídele a tu asistente de IA: "Crea un archivo Python `traductor_emoji.py`. Debe incluir un diccionario `TEXTO_A_EMOJI` con al menos 10 mapeos de palabras a emojis. Luego, crea una función `traducir_a_emoji(texto)` que tome un string, lo divida en palabras y reemplace las palabras conocidas con sus emojis. También, crea una función `traducir_a_texto(emojis)` que haga lo inverso. Finalmente, muestra cómo usar ambas funciones con un ejemplo."
    *   Asegúrate de que el script incluya un ejemplo de cómo invertir el diccionario `TEXTO_A_EMOJI` para crear `EMOJI_A_TEXTO` automáticamente.

2.  **Expande el diccionario:**
    *   ¡Tu diccionario es muy pequeño! Pídele a la IA: "Sugiere 20 pares palabra-emoji comunes para añadir al diccionario `TEXTO_A_EMOJI` en `traductor_emoji.py`."
    *   Pídele que te ayude a actualizar el script con estas nuevas adiciones.

3.  **Mejora la traducción:**
    *   **Manejo de mayúsculas/minúsculas:** Actualmente, la traducción distingue entre "Feliz" y "feliz". Pídele a la IA: "Modifica `traducir_a_emoji` para que no sea sensible a mayúsculas y minúsculas en el texto de entrada."
    *   **Palabras no encontradas:** ¿Qué pasa si una palabra no está en el diccionario? ¿O un emoji no está mapeado? Dile a la IA: "Mejora las funciones de traducción para que, si una palabra o emoji no se encuentra en el diccionario, se mantenga el original en la salida en lugar de omitirlo."
    *   **Múltiples palabras para un emoji (o viceversa):** Pregunta a la IA: "¿Cómo podría modificar el sistema para que varias palabras (por ejemplo, 'dinero', 'plata', 'efectivo') se traduzcan al mismo emoji (💰)? ¿Y cómo manejaría la traducción inversa?" (Esto puede requerir cambios en la estructura de datos).

4.  **Crea una interfaz de usuario simple:**
    *   Pídele a la IA: "Añade un bucle principal en `traductor_emoji.py` que le pregunte al usuario si quiere traducir de texto a emoji o de emoji a texto, luego le pida la entrada y muestre la traducción, repitiendo hasta que el usuario decida salir."

5.  **Traducción Inteligente con LLMs (Desafío Avanzado):**
    *   Los diccionarios son limitados. Para una traducción emoji que entienda el contexto y el sentimiento, ¡un LLM es ideal! Investiga o pregunta a tu IA: "¿Cómo puedo usar una API de LLM para traducir una frase a una secuencia de emojis que representen su significado de forma creativa? Proporcióname un ejemplo en Python."
    *   De forma similar, explora: "¿Puede un LLM interpretar una secuencia de emojis y traducirla a una frase coherente en lenguaje natural?"

**Objetivo:**
Este demo te enseña cómo la IA puede ayudar en tareas de mapeo de datos, generación de código repetitivo (como expandir diccionarios) y en la lógica de procesamiento de strings. ¡Diviértete creando un traductor único! 