import sys

from stats import (
    get_book_text,
    get_num_words,
    count_chars,
    dict_to_list
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text_to_str = get_book_text(book_path)
    num_words = get_num_words(text_to_str)

    char_dict = count_chars(text_to_str)
    sorted_char_dict = dict_to_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dictionary in sorted_char_dict:
        if dictionary['char'].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")

    print("============= END ===============")

if __name__ == '__main__':
    main()