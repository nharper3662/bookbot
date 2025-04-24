from stats import get_word_count, character_count, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(text):
    with open(text) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_dict = character_count(book_text)
    sorted_dict = sort_dict(character_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_dict:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print ("============= END ===============")
            

main()