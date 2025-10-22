def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(text_string):
    return(len(text_string.split()))

#######################################

def main(path_to_book):
    print(f"Found {word_counter(get_book_text(path_to_book))} total words")

main("books/frankenstein.txt")