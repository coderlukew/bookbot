from stats import count_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents



def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    charc_count = count_characters(book)
    print(f"{num_words} words found in the document")
    print(charc_count)

main()
