PALABRAS_POSITIVAS = ["feliz", "genial", "increíble", "amor", "bueno", "excelente", "fantástico", "alegre", "disfrutar", "alegría", "bendición", "brillante", "celebrar", "confianza", "diversión", "encantado", "esperanza", "éxito", "fascinante", "fortuna", "gratitud", "inspirador", "maravilloso", "optimista"]
PALABRAS_NEGATIVAS = ["triste", "terrible", "odio", "malo", "pésimo", "aburrido", "problema", "difícil", "ansiedad", "decepción", "desgracia", "dolor", "enfado", "fracaso", "frustración", "ira", "lástima", "miedo", "negativo", "pesimismo", "preocupación", "rechazo", "rencor"]

import google.generativeai as genai
import os

# Intenta importar la clave API desde gemini_config.py
# Esto es para mantener la clave API separada del código principal.
# Asegúrate de que gemini_config.py esté en el mismo directorio o en sys.path
# y que contenga una variable API_KEY = "tu_clave_aqui"

try:
    from . import gemini_config # Para ejecución como parte de un paquete
except ImportError:
    try:
        import gemini_config # Para ejecución directa del script
    except ImportError:
        gemini_config = None

gemini_api_configured = False # Flag to indicate if API is configured

if gemini_config and hasattr(gemini_config, 'API_KEY') and gemini_config.API_KEY != "TU_API_KEY_AQUI" and gemini_config.API_KEY:
    try:
        genai.configure(api_key=gemini_config.API_KEY)
        gemini_api_configured = True
    except Exception as e:
        print(f"Error configurando Gemini API desde gemini_config.py: {e}")
else:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if GOOGLE_API_KEY:
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            gemini_api_configured = True
        except Exception as e:
            print(f"Error configurando Gemini API desde variable de entorno: {e}")

if not gemini_api_configured:
    print("Advertencia: Clave API de Gemini no configurada o la configuración falló. La función 'analizar_sentimiento_gemini' no funcionará.")
    print("Por favor, verifica tu archivo 'gemini_config.py' o la variable de entorno GOOGLE_API_KEY.")

def analizar_sentimiento(texto):
    """Analiza el sentimiento de un texto basado en las palabras positivas y negativas."""
    score_positivo = 0
    score_negativo = 0
    total_palabras_con_sentimiento = 0

    palabras = texto.lower().split()
    for palabra in palabras:
        if palabra in PALABRAS_POSITIVAS:
            score_positivo += 1
            total_palabras_con_sentimiento += 1
        elif palabra in PALABRAS_NEGATIVAS:
            score_negativo += 1
            total_palabras_con_sentimiento += 1

    if total_palabras_con_sentimiento == 0:
        return 0

    puntaje = (score_positivo - score_negativo) / total_palabras_con_sentimiento
    return puntaje

def analizar_sentimiento_gemini(texto):
    """Analiza el sentimiento de un texto usando la API de Google Gemini."""
    if not gemini_api_configured:
        return "Error: API Key de Gemini no configurada o la configuración falló."

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        # Prompt mejorado para solicitar sentimiento y una breve justificación.
        # También se le pide un formato más estructurado para facilitar el parsing.
        prompt = f"""Analiza el sentimiento del siguiente texto. 
        Clasifícalo como Positivo, Negativo o Neutral. 
        Opcionalmente, si es posible, identifica emociones más específicas (ej: alegría, enojo, sorpresa) y la intensidad (ej: leve, moderado, fuerte).
        Proporciona una breve justificación para tu clasificación.
        Formato de respuesta deseado:
        Sentimiento: [Positivo/Negativo/Neutral]
        Emociones Específicas: [lista de emociones o N/A]
        Intensidad: [Leve/Moderado/Fuerte o N/A]
        Justificación: [Tu justificación]

        Texto a analizar: "{texto}"
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al contactar la API de Gemini: {e}"

# Ejemplo de uso
frase1 = "Me siento increíble y feliz hoy."
frase2 = "Estoy triste y aburrido."
frase3 = "Tengo un problema."
frase4 = "Me encanta la vida."
frase5 = "No puedo creer lo malo que fue."

print(f"'{frase1}' -> {analizar_sentimiento(frase1)}") # Esperado: Positivo o cercano a 1 
print(f"'{frase2}' -> {analizar_sentimiento(frase2)}") # Esperado: Negativo o cercano a -1
print(f"'{frase3}' -> {analizar_sentimiento(frase3)}") # Esperado: Negativo o cercano a -1
print(f"'{frase4}' -> {analizar_sentimiento(frase4)}") # Esperado: Positivo o cercano a 1
print(f"'{frase5}' -> {analizar_sentimiento(frase5)}") # Esperado: Negativo o cercano a -1 

print("\n--- Análisis con Gemini API ---")
if gemini_api_configured: # Solo ejecutar si la API key está configurada y la configuración fue exitosa
    frase_gemini_1 = "Estoy absolutamente encantado con el resultado, ¡es fantástico!"
    frase_gemini_2 = "Qué día tan terrible, todo salió mal."
    frase_gemini_3 = "El evento fue simplemente aceptable, ni bueno ni malo."
    frase_gemini_4 = "No puedo creer lo maravilloso que fue ese gesto, estoy muy agradecido."
    frase_gemini_5 = "Siento una profunda tristeza y decepción por lo ocurrido."
    frase_gemini_6 = "Sinceramente? Ando de la perra, manito"

    print(f"Análisis de '{frase_gemini_1}':")
    print(analizar_sentimiento_gemini(frase_gemini_1))
    print("-----")
    print(f"Análisis de '{frase_gemini_2}':")
    print(analizar_sentimiento_gemini(frase_gemini_2))
    print("-----")
    print(f"Análisis de '{frase_gemini_3}':")
    print(analizar_sentimiento_gemini(frase_gemini_3))
    print("-----")
    print(f"Análisis de '{frase_gemini_4}':")
    print(analizar_sentimiento_gemini(frase_gemini_4))
    print("-----")
    print(f"Análisis de '{frase_gemini_5}':")
    print(analizar_sentimiento_gemini(frase_gemini_5))
    print("-----")
    print(f"Análisis de '{frase_gemini_6}':")
    print(analizar_sentimiento_gemini(frase_gemini_6))
    print("--------------------------------")
    
else:
    print("Ejemplos de Gemini API omitidos debido a la falta de configuración de la API key o error en la configuración.")
