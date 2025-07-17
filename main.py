import sys

from stats import print_book_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_book_report(sys.argv[1])

main()
