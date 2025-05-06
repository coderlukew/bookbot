def count_words(text):
    words = text.split()
    return len(words)


def count_characters(input):
    text = input.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

