def get_book_text(file):
    with open(file) as f:
        return f.read()


def get_num_words(text):
        word_list = text.split()

        return len(word_list)


def count_chars(text):
    chars = {}

    for c in text:
        lowered = c.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def sort_on(d):
    return d['num']


def dict_to_list(dictionary):
    dict_list = []

    for key in dictionary:
        dict_list.append({'char': key, 'num': dictionary[key]})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list