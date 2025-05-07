def count_words(text):
    words = text.split()
    return len(words)


def count_characters(input):
    text = input.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def sort_char_counts(char_count_dict):
    # Convert dictionary to list of dictionaries with "char" and "num" keys
    char_list = [
        {"char": char, "num": count}
        for char, count in char_count_dict.items()
        if char.isalpha()
    ]
    
    # Sort the list by "num" in descending order
    return sorted(char_list, key=lambda x: x["num"], reverse=True)