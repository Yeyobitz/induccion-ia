# Demo 2: Generador de Historias Cortas

¡Hola, futuro escritor! Prepárate para crear historias con IA.

**Concepto:**
Este demo te permite generar el inicio de una historia corta a partir de una idea o "prompt" que tú proporciones. Tu tarea será usar IA para expandir y mejorar el generador.

**Estado Actual:**
No hay código aún. ¡Ese es tu primer desafío con la IA!

**Tu Misión (con ayuda de la IA):**

1.  **Crea el script base:**
    *   Pídele a tu IA: "Crea un script de Python llamado `generador_historias.py`. Debe tener una función `generar_historia(prompt)` que tome un string como `prompt` y devuelva un string con un párrafo inicial de una historia basada en ese prompt. Por ahora, la función puede devolver un texto fijo como: 'Érase una vez en un {prompt}, un valiente caballero...' para probar."
    *   Añade un código simple para pedirle al usuario un `prompt` y luego llamar a la función e imprimir la historia.

2.  **Integración con una API de LLM para generación de texto:**
    *   El verdadero poder de la IA generativa para historias reside en los Modelos de Lenguaje Grandes (LLMs). Investiga (busca en internet o pídele a tu IA): "¿Cómo usar APIs de LLMs como OpenAI GPT, Gemini, o Claude desde Python para generar texto creativo a partir de un prompt?".
    *   Modifica tu función `generar_historia(prompt)` para que, en lugar de devolver un texto fijo, llame a la API del LLM con el `prompt` del usuario y devuelva la respuesta de la IA. ¡Aquí es donde tu generador se volverá mucho más interesante!

3.  **Mejora la calidad de la generación (con LLMs):**
    *   Experimenta con diferentes `prompts`. ¿Qué tipo de `prompts` generan mejores historias con el LLM?
    *   Pídele a la IA: "¿Cómo puedo mejorar mis `prompts` para obtener historias más creativas/divertidas/de terror del LLM? Dame ejemplos de técnicas de prompting avanzado."

4.  **Añade características:**
    *   **Elección de género:** Pídele a la IA: "Modifica `generador_historias.py` para que el usuario pueda elegir un género (fantasía, ciencia ficción, comedia) y el `prompt` se adapte o se añada información al `prompt` enviado a la IA para que genere una historia de ese género."
    *   **Generación de personajes:** Pregunta a la IA: "¿Cómo podría añadir una función que genere nombres y descripciones cortas de personajes para incluir en la historia?"
    *   **Continuación de historias:** Dile a la IA: "Quiero que el usuario pueda tomar una historia generada y pedirle a la IA que escriba el siguiente párrafo. ¿Cómo modifico el script para esto?"

**Objetivo:**
Descubrir cómo la IA puede ser una herramienta poderosa para la creatividad, ayudándote a generar borradores, explorar ideas y superar el bloqueo del escritor. Aprende a interactuar con APIs de IA y a refinar los `prompts` para obtener los resultados deseados. 