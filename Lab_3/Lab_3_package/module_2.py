from deep_translator import GoogleTranslator, single_detection
from .enums import LangSet, OutResult
import pandas as pd

def translate(text, src, dest):
    dest_code = code_lang(dest)

    if dest_code:
        try:
            translation = GoogleTranslator(source='auto', target=dest_code).translate(text)
            return translation
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Invalid language code or name."


def lang_detect(text, set=LangSet.lang):
    try:
        detection = single_detection(text, api_key=None)

        if set == LangSet.lang:
            return detection

        if set == LangSet.confidence:
            return 0

        return {
            "language": detection,
            "confidence": 0
        }
    except Exception as e:
        return f"Error: {str(e)}"

def code_lang(lang):
    lang = lang.lower()
    translator = GoogleTranslator()

    if lang in translator.get_supported_languages(as_dict=True).keys():
        return lang

    for code, name in translator.get_supported_languages(as_dict=True).items():
        if name.lower() == lang:
            return code

    return None

def language_list(out, text):
    try:
        data = []

        for lang_dest in GoogleTranslator.get_supported_languages(as_dict=True).keys():
            lang_name = GoogleTranslator.get_supported_languages(as_dict=True)[lang_dest].capitalize()
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
