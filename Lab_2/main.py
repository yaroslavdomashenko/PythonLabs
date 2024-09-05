from googletrans import Translator, LANGUAGES

def Translate(text, lang):
    translator = Translator()

    lang_code = Codelang(lang)

    if lang_code:
        try:
            translation = translator.translate(text, dest=lang_code)
            return translation.text
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Invalid language code or name."

def LangDetect(text):
    translator = Translator()
    try:
        detection = translator.detect(text)
        return detection.lang
    except Exception as e:
        return f"Error: {str(e)}"

def Codelang(lang):
    lang = lang.lower()

    if lang in LANGUAGES.keys():
        return lang

    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code

    return None


def main():
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language: ")

    translated_text = Translate(text, target_lang)
    print(f"Translated text: {translated_text}")

    detected_lang = LangDetect(text)
    print(f"Detected Language: {detected_lang}")


if __name__ == "__main__":
    main()

