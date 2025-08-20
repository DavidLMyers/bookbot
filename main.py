import sys
from stats import get_word_count, get_letter_count, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def output(file_path, word_count, letter_count_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in letter_count_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    letter_count_sorted = sort_dict(letter_count)
    output(file_path, word_count, letter_count_sorted)


main()