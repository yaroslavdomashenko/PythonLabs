from googletrans import Translator, LANGUAGES
from .enums import LangSet, OutResult
import pandas as pd

def translate(text, scr, dest):
    translator = Translator()

    dest_code = code_lang(dest)

    if dest_code:
        try:
            translation = translator.translate(text, dest=dest_code)
            return translation.text
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Invalid language code or name."

def lang_detect(text, set=LangSet.lang):
    translator = Translator()
    try:
        detection = translator.detect(text)

        if set == LangSet.lang:
            return detection.lang

        if set == LangSet.confidence:
            return detection.confidence

        return {
            "language": detection.lang,
            "confidence": detection.confidence
        }
    except Exception as e:
        return f"Error: {str(e)}"

def code_lang(lang):
    lang = lang.lower()

    if lang in LANGUAGES.keys():
        return lang

    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code

    return None

def language_list(out, text):
    try:
        data = []

        for lang_dest in LANGUAGES.keys():
            lang_name = LANGUAGES[lang_dest].capitalize()
            translated_text = ""
            lang_src = lang_detect(text, LangSet.lang)

            if text:
                translated_text = translate(text, lang_src, lang_dest)

            data.append({
                "language": lang_name,
                "iso": lang_dest,
                "text": translated_text if text else ""
            })

        df = pd.DataFrame(data)

        if out == OutResult.screen:
            print(df)
        elif out == "file":
            filename = "languages_list.csv"
            df.to_csv(filename, index=False)
            print(f"Table has been saved to {filename}")
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"