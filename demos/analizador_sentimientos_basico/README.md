# Demo 4: Analizador de Sentimientos Básico

Descubre las emociones ocultas en el texto con IA.

**Concepto:**
Este proyecto te introduce al análisis de sentimientos. Crearás una herramienta que intente determinar si un fragmento de texto tiene una connotación positiva, negativa o neutral.

**Estado Actual:**
Empezarás con un enfoque muy simple basado en palabras clave. La IA te ayudará a construirlo y luego a mejorarlo.

```python
# analizador_sentimientos.py (esqueleto inicial que puedes pedir a la IA)

PALABRAS_POSITIVAS = ["feliz", "genial", "increíble", "amor", "bueno", "excelente", "fantástico", "alegre", "disfrutar"]
PALABRAS_NEGATIVAS = ["triste", "terrible", "odio", "malo", "pésimo", "aburrido", "problema", "difícil"]

def analizar_sentimiento(texto):
    texto = texto.lower()
    score_positivo = 0
    score_negativo = 0

    palabras = texto.split() # Podrías pedirle a la IA que mejore la tokenización

    for palabra in palabras:
        palabra_limpia = ''.join(filter(str.isalnum, palabra)) # Limpieza básica
        if palabra_limpia in PALABRAS_POSITIVAS:
            score_positivo += 1
        elif palabra_limpia in PALABRAS_NEGATIVAS:
            score_negativo += 1

    if score_positivo > score_negativo:
        return "Positivo"
    elif score_negativo > score_positivo:
        return "Negativo"
    else:
        return "Neutral"

# Ejemplo de uso (pídele a la IA que cree una interfaz de consola)
# frase1 = "Me siento increíble y feliz hoy."
# frase2 = "Este es un problema terrible y malo."
# frase3 = "El cielo es azul."

# print(f"'{frase1}' -> {analizar_sentimiento(frase1)}")
# print(f"'{frase2}' -> {analizar_sentimiento(frase2)}")
# print(f"'{frase3}' -> {analizar_sentimiento(frase3)}")
```

**Tu Misión (con ayuda de la IA):**

1.  **Genera el script `analizador_sentimientos.py`:**
    *   Pídele a tu asistente de IA: "Crea un archivo Python `analizador_sentimientos.py`. Define dos listas: `PALABRAS_POSITIVAS` y `PALABRAS_NEGATIVAS` con al menos 5 ejemplos cada una. Luego, crea una función `analizar_sentimiento(texto)` que cuente cuántas palabras positivas y negativas hay en el texto (ignorando mayúsculas/minúsculas y puntuación básica) y devuelva 'Positivo', 'Negativo' o 'Neutral' según el conteo. Incluye ejemplos de uso."

2.  **Expande las listas de palabras:**
    *   Pídele a la IA: "Sugiere 15 palabras positivas y 15 palabras negativas más para añadir a las listas en `analizador_sentimientos.py`."
    *   Actualiza tu script con estas nuevas palabras.

3.  **Mejora el análisis:**
    *   **Puntuación más granular:** En lugar de solo "Positivo/Negativo/Neutral", ¿cómo podrías devolver un puntaje numérico (por ejemplo, de -1 a 1)? Pídele a la IA: "Modifica `analizar_sentimiento` para que devuelva un puntaje numérico de sentimiento, donde los números más altos son más positivos y los más bajos más negativos."
    *   **Manejo de negaciones:** El actual analizador no maneja bien frases como "no estoy feliz". Pregúntale a la IA: "¿Cómo podría modificar el analizador para que detecte negaciones simples (como 'no') antes de una palabra positiva o negativa e invierta su polaridad?"
    *   **Uso de bibliotecas de NLP (Natural Language Processing):** Para un análisis más robusto, existen bibliotecas especializadas. Pídele a la IA: "¿Qué bibliotecas de Python populares existen para análisis de sentimientos? Muéstrame un ejemplo simple de cómo usar una de ellas (por ejemplo, NLTK con VADER, o TextBlob) para analizar el sentimiento de una frase."
        *   Si te animas, intenta reemplazar tu analizador basado en palabras clave con uno que use una de estas bibliotecas.
    *   **Análisis de Sentimientos con LLMs (Nivel Superior):** Las bibliotecas de NLP son buenas, pero los LLMs pueden ofrecer un análisis de sentimientos aún más matizado y consciente del contexto. Investiga (o pide a tu IA): "¿Cómo puedo usar una API de LLM (como Gemini, GPT, etc.) para realizar análisis de sentimientos en Python? ¿Puede detectar emociones más específicas o la intensidad del sentimiento?". Considera esto como un paso avanzado para mejorar radicalmente tu analizador.

4.  **Aplica tu analizador:**
    *   Piensa en dónde podrías usar este analizador. ¿Analizar reseñas de productos? ¿Comentarios en redes sociales? Pídele a la IA que te ayude a escribir un script que lea varias frases de un archivo de texto (una por línea) y guarde los resultados del análisis en otro archivo.

**Objetivo:**
Aprender los conceptos básicos del análisis de sentimientos, desde enfoques simples basados en diccionarios hasta el uso de bibliotecas de NLP más potentes. Descubrir cómo la IA puede ayudar a procesar y entender el lenguaje humano. 