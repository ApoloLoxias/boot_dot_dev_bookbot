from stats import word_counter

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#######################################

def main(path_to_book):
    print(f"Found {word_counter(get_book_text(path_to_book))} total words")

main("books/frankenstein.txt")