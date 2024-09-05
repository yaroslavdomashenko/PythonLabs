from Lab_3_package.enums import OutResult
from Lab_3_package.module_2 import translate, language_list

def main():
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language: ")

    translated_text = translate(text, "", target_lang)
    print(f"Translated text: {translated_text}")

    print("Table:")
    language_list(OutResult.screen, text)

if __name__ == "__main__":
    main()
