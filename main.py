from stats import get_num_words
from stats import get_letter_counts
from stats import convert_dict

def get_book_text(file_name):
    with open(file_name) as f:
        return f.read()


def main():
    book = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book}...')
    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    sort_dict = convert_dict(get_letter_counts(book))
    for item in sort_dict:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()
