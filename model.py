from deep_translator import GoogleTranslator

sentence = "Hola, cómo estás."  # Replace this with your sentence

target = ''
g_trans = GoogleTranslator(target='en')

translated_text = g_trans.translate(sentence)  # 'en' for English



