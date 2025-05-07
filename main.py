from stats import count_words, count_characters, sort_char_counts
import sys



def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents



def main():
    # Check if sys.argv has exactly 2 entries (script name + file path)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Store the second argument (file path) in a variable
    book_path = sys.argv[1]
    
    book = get_book_text(book_path)
    num_words = count_words(book)
    charc_count = count_characters(book)
    sorted = sort_char_counts(charc_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f" Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        print(f" {entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
