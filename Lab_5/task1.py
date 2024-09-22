import string

def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence = text.split('.')[0]
            print("Перше речення:", first_sentence)

            translator = str.maketrans('', '', string.punctuation)
            clean_text = text.translate(translator)

            words = clean_text.split()

            ukrainian_words = sorted([word for word in words if word.isalpha() and is_ukrainian(word)])
            english_words = sorted([word for word in words if word.isalpha() and is_english(word)])

            print("Українські слова по алфавіту:", ukrainian_words, "\n")
            print("Англійські слова по алфавіту:", english_words, "\n")
            print("Загальна кількість слів у тексті:", len(words))

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def is_ukrainian(word):
    ukrainian_chars = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return any(char in ukrainian_chars for char in word.lower())

def is_english(word):
    return all('a' <= char <= 'z' for char in word.lower())


if __name__ == '__main__':
    read_first_sentence('text.txt')
