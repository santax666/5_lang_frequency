import re
from collections import Counter


def load_data(filepath):
    # чтение файла в WIN-кодировке
    return open(filepath, 'r', encoding="cp1251")


def get_most_frequent_words(text):
    tekst = (text.read()).lower()  # перевести весь текст в нижний регистр
    result = re.findall(r'\w+', tekst)  # поиск слов с сохранением в список
    for ind, slovo in enumerate(result):  # просмотр всех слов
        if not slovo.isalpha():  # если слово содержит цифру, удаляем из списка
            del result[ind]
    # возвращает список 10 популярных слов
    return Counter(result).most_common(10)

if __name__ == '__main__':
    f = load_data('tolstoi_l_n__voina_i_mir.txt')
    popular_words = get_most_frequent_words(f)
    print("10 самых популярных слов в этом файле:")
    for words in popular_words:
        print("==> слово '", words[0], "' частота - ", words[1])
