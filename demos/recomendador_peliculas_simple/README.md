# Demo 5: Recomendador de Películas Simple

¡Ayuda a los usuarios a encontrar su próxima película favorita con IA!

**Concepto:**
Construirás un sistema básico de recomendación de películas. Empezarás con una lista fija de películas y géneros, y luego usarás la IA para hacerlo más inteligente y dinámico.

**Estado Actual:**
Tendrás que pedirle a la IA que genere la estructura inicial con algunas películas de ejemplo.

```python
# recomendador_peliculas.py (esqueleto inicial que puedes pedir a la IA)

PELICULAS = {
    "The Matrix": {"genero": "Ciencia Ficción", "rating": 8.7, "keywords": ["ia", "distopia", "accion"]},
    "Interestelar": {"genero": "Ciencia Ficción", "rating": 8.6, "keywords": ["espacio", "tiempo", "drama"]},
    "El Padrino": {"genero": "Drama", "rating": 9.2, "keywords": ["mafia", "crimen", "familia"]},
    "Batman: El Caballero de la Noche": {"genero": "Acción", "rating": 9.0, "keywords": ["superheroes", "crimen", "oscuridad"]},
    "Tiempos Violentos": {"genero": "Crimen", "rating": 8.9, "keywords": ["dialogo", "no lineal", "violencia"]},
    "Forrest Gump": {"genero": "Drama", "rating": 8.8, "keywords": ["historia", "vida", "superacion"]},
    "Amelie": {"genero": "Comedia", "rating": 8.3, "keywords": ["paris", "romance", "peculiar"]},
    "El Viaje de Chihiro": {"genero": "Animación", "rating": 8.6, "keywords": ["espiritus", "aventura", "ghibli"]}
    # ¡Pídele a la IA que añada más!
}

def recomendar_por_genero(genero_preferido, peliculas_data):
    recomendaciones = []
    for titulo, detalles in peliculas_data.items():
        if detalles["genero"].lower() == genero_preferido.lower():
            recomendaciones.append(titulo)
    return recomendaciones if recomendaciones else ["No se encontraron películas de ese género."]

def recomendar_por_keyword(keyword, peliculas_data):
    recomendaciones = []
    for titulo, detalles in peliculas_data.items():
        if keyword.lower() in [k.lower() for k in detalles["keywords"]]:
            recomendaciones.append(titulo)
    return recomendaciones if recomendaciones else ["No se encontraron películas con esa palabra clave."]

# Ejemplo de uso (pídele a la IA que cree una interfaz de consola)
# genero_usuario = "Ciencia Ficción"
# print(f"Películas de {genero_usuario}: {recomendar_por_genero(genero_usuario, PELICULAS)}")

# keyword_usuario = "espacio"
# print(f"Películas sobre '{keyword_usuario}': {recomendar_por_keyword(keyword_usuario, PELICULAS)}")
```

**Tu Misión (con ayuda de la IA):**

1.  **Genera el script `recomendador_peliculas.py`:**
    *   Pídele a tu asistente de IA: "Crea un archivo Python `recomendador_peliculas.py`. Define un diccionario llamado `PELICULAS` donde cada clave es un título de película y el valor es otro diccionario con 'genero', 'rating' (un float) y 'keywords' (una lista de strings). Incluye al menos 5 películas. Luego, crea una función `recomendar_por_genero(genero, datos_peliculas)` que devuelva una lista de películas de ese género, y otra `recomendar_por_keyword(keyword, datos_peliculas)`. Muestra cómo usarlas."

2.  **Expande la base de datos de películas:**
    *   Pídele a la IA: "Sugiere 10 películas más con sus géneros, ratings (inventados si es necesario) y 3-4 keywords relevantes para añadir al diccionario `PELICULAS`."
    *   Actualiza tu script con esta información.

3.  **Mejora las recomendaciones:**
    *   **Recomendaciones basadas en similitud (simple):** Pregunta a la IA: "Si a un usuario le gustó 'The Matrix', ¿cómo podría encontrar películas similares basándome en el género y las keywords compartidas? Ayúdame a escribir una función `recomendar_similares(titulo_pelicula, datos_peliculas)`."
    *   **Filtrar por rating:** Pídele a la IA: "Modifica las funciones de recomendación para que solo sugieran películas con un rating mayor a un umbral que elija el usuario (por ejemplo, mayor a 8.0)."
    *   **Obtener datos de películas de una API (avanzado):** Investiga (con ayuda de la IA) si existen APIs gratuitas para obtener información de películas (como The Movie Database - TMDB). Pídele a la IA: "Muéstrame un ejemplo de cómo obtener el género y las keywords de una película usando la API de TMDB en Python." Si te animas, intenta modificar tu script para buscar películas usando una API en lugar de tenerlas en un diccionario fijo.

4.  **Crea una interfaz de usuario interactiva:**
    *   Pídele a la IA: "Crea un menú en la consola para que el usuario pueda elegir si quiere recomendaciones por género, por keyword, o encontrar películas similares a una que le guste. El sistema debe pedir la entrada necesaria y mostrar las recomendaciones."

5.  **Recomendaciones Avanzadas con LLMs (Desafío Creativo):**
    *   ¿Cómo podrían los LLMs mejorar tu recomendador? Investiga o consulta a tu IA:
        *   "¿Puede un LLM ayudarme a generar descripciones de películas más atractivas o resúmenes personalizados basados en las preferencias de un usuario?"
        *   "¿Podría usar un LLM para que un usuario pida recomendaciones en lenguaje natural, como 'sugiéreme una película de ciencia ficción espacial que no sea muy oscura y tenga buenos efectos especiales'?"
        *   "¿Cómo podría un LLM ayudar a encontrar películas 'similares' de una manera más matizada que solo por keywords o género, quizás entendiendo el 'ambiente' o 'estilo' de una película?"
    *   Experimenta integrando una API de LLM para alguna de estas ideas.

**Objetivo:**
Explorar cómo se pueden construir sistemas de recomendación simples y cómo la IA puede ayudar a generar datos de ejemplo, mejorar la lógica de recomendación e incluso interactuar con fuentes de datos externas para hacer las recomendaciones más ricas y relevantes. 