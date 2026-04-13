from deep_translator import GoogleTranslator

texto_ingles = "Hello, how are you?"
# Traducir de inglés a español
traduccion = GoogleTranslator(source='en', target='es').translate(texto_ingles)

print(traduccion) # Salida: Hola, ¿cómo estás?


