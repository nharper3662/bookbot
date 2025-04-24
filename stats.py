def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def character_count(text):
    lowercase_text = text.lower()
    char_counts = {}
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_dict(dictionary):
    char_list = []
    for char, count in dictionary.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list