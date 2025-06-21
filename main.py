import sys
from stats import get_num_words, get_num_characters, get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_source = sys.argv[1]
    contents = get_book_text(book_source)
    num_words = get_num_words(contents)
    num_characters = get_num_characters(contents)
    sorted_list = get_sorted_list(num_characters)
    sorted_list_of_letters = [item for item in sorted_list if item["char"].isalpha()]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_source}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for item in sorted_list_of_letters:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()