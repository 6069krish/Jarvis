from googletrans import Translator

translator = Translator()
input("Please enter the text to translate.")
text_to_translate = input("You: ")
    
input("Please enter the language code for translation. For example, 'fr' for French.")
target_language = input("You: ")

translation = translator.translate(text_to_translate, dest=target_language)
translated_text = translation.text

print("Translated text is: " + translated_text)