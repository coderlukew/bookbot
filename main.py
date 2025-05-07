from stats import count_words, count_characters, sort_char_counts


def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents



def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    charc_count = count_characters(book)
    sorted = sort_char_counts(charc_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f" Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        print(f" '{entry['char']}': {entry['num']}")
    print("============= END ===============")

main()
