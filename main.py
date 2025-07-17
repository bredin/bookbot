from stats import print_book_report

import sys

def get_book_text(file_name):
    with open(file_name) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_book_report(sys.argv[1])


main()
