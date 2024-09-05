import csv
import os
import pandas as pd

from Lab_3.lab3_package.module_1 import translate, lang_detect

def read_config(config_file):
    try:
        with open(config_file, 'r') as file:
            reader = csv.reader(file)
            config = next(reader)
            return {
                'text_file': config[0],
                'target_language': config[1],
                'output': config[2],
                'char_limit': int(config[3]) + 1,
                'word_limit': int(config[4]) + 1,
                'sentence_limit': int(config[5]) + 1
            }
    except Exception as e:
        print(f"Error reading configuration file: {str(e)}")
        return None

def get_text_statistics(text):
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    return char_count, word_count, sentence_count

def read_and_process_text(text_file, char_limit, word_limit, sentence_limit):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

            print(type(text))

            text = '.'.join(text.split('.')[:sentence_limit])

            text = ' '.join(text.split(' ')[:word_limit])

            text = text[:char_limit]

            return text
    except Exception as e:
        print(f"Error reading text file: {str(e)}")
        return None

def output_result(translated_text, output_method, original_file, target_language):
    if output_method == 'screen':
        print(f"Translated text to {target_language}:\n{translated_text}")
    elif output_method == 'file':
        output_file = f"{os.path.splitext(original_file)[0]}_{target_language}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        except Exception as e:
            print(f"Error writing to file: {str(e)}")
    else:
        print("Invalid output method specified in configuration.")


def main():
    config_file = 'config.csv'
    config = read_config(config_file)
    if not config:
        return

    if not os.path.isfile(config['text_file']):
        print(f"File '{config['text_file']}' not found.")
        return

    with open(config['text_file'], 'r', encoding='utf-8') as f:
        content = f.read()

    file_size = os.path.getsize(config['text_file'])
    char_count, word_count, sentence_count = get_text_statistics(content)
    detected_language = lang_detect(content)

    print(pd.DataFrame([{
        "File Name": config['text_file'],
        "File Size": f"{file_size} bytes",
        "Character Count": f"{char_count} characters",
        'Word Count': f"{word_count} words",
        "Sentence Count": f"{sentence_count} sentences",
        "Detected Language": detected_language
    }]))

    text = read_and_process_text(config['text_file'], config['char_limit'], config['word_limit'], config['sentence_limit'])

    if text is None:
        return

    translated_text = translate(text, "", config['target_language'])

    if not translated_text:
        return

    output_result(translated_text, config['output'], config['text_file'], config['target_language'])


if __name__ == "__main__":
    main()
