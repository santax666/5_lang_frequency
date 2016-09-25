import re
from collections import Counter
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding="cp1251") as file_handler:
        lowercase_text = (file_handler.read()).lower()
        return lowercase_text


def get_most_frequent_words(text):
    find_only_words = re.findall(r'\w+', text)
    for word_number, word in enumerate(find_only_words):
        if not word.isalpha():
            del find_only_words[word_number]
    return Counter(find_only_words).most_common(number_of_popular_words)

if __name__ == '__main__':
    number_of_popular_words = 10
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("Скрипт выводит 10 самых популярных слов в текстовом файле")
            print("Введите в терминале: python3.5 lang_frequency.py file.txt")
        else:
            text_file = load_data(sys.argv[1])
            if text_file is None:
                print("Текстовый файл не обнаружен!")
            else:
                popular_words = get_most_frequent_words(text_file)
                print(number_of_popular_words, 'самых популярных слов:')
                for words in popular_words:
                    print("==> слово '", words[0], "' частота - ", words[1])
    else:
        print("Не задан файл для вывода!")
