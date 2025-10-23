from stats import word_counter, key_counter

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def list_chars(string):
    separator = "super_special_separator_that_is_highly_unlikely_to_naturaly_appear_in_a_given_written_text_'Rq9*c8;tCI9"
    return separator.join(string).split(separator)

#######################################

"""
# Main fuction that prints how many words there are in the book
def main(path_to_book):
    print(f"Found {word_counter(get_book_text(path_to_book))} total words")
"""
#main("books/frankenstein.txt")

# print(list_chars(get_book_text("books/test"))) # gets book and makes list with all characters
# print(key_counter(list_chars(get_book_text("books/test")))) # gets book and counts characters
# print(get_book_text("books/test").lower()) # prints book text in lowercase
# print(key_counter(list_chars(get_book_text("books/test").lower()))) # gets book and counts characters, case insensitive

"""
Main function that prints dictionary with how many times each charcter appears
def main(path_to_book):
    print(key_counter(list_chars(get_book_text(path_to_book).lower())))
"""
# main("books/frankenstein.txt")
def main(path_to_book):
    print(f"Found {word_counter(get_book_text(path_to_book))} total words")
    print(key_counter(list_chars(get_book_text(path_to_book).lower())))

main("books/frankenstein.txt")