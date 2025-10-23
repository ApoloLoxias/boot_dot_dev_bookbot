from stats import word_counter, key_counter, sort_dic, sort_alpha

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def list_chars(string):
    separator = "super_special_separator_that_is_highly_unlikely_to_naturaly_appear_in_a_given_written_text_'Rq9*c8;tCI9"
    return separator.join(string).split(separator)

def pretty_printer(sorted_list_of_dics):
    for dic in sorted_list_of_dics:
        print(f"{dic["char"]}: {dic["count"]}")
# ======================================================================
"""
def main(path_to_book):
    book_text_in_lower_case = get_book_text(path_to_book).lower()
    print(f"Found {word_counter(book_text_in_lower_case)} total words")
    print(key_counter(list_chars(book_text_in_lower_case)))
"""
# =====================================================================
"""
def main(path_to_book):
    book_text_in_lower_case = get_book_text(path_to_book).lower()
    print(f"Found {word_counter(book_text_in_lower_case)} total words")
    #counted_char_dic = key_counter(list_chars(book_text_in_lower_case))
    #print(sort_dic(counted_char_dic))
    #print(sort_dic(key_counter(list_chars(book_text_in_lower_case))))
    #print(sort_alpha(key_counter(list_chars(book_text_in_lower_case))))
    pretty_printer(sort_alpha(key_counter(list_chars(book_text_in_lower_case))))
"""
# ======================================================================

def main(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")

    print("--------- Character Count -------")

    print("============= END ===============")
# ======================================================================
main("books/frankenstein.txt")
# sorted_list_of_dics = [{"char": "a", "count": 3}, {"char": "b", "count": 2}]
# pretty_printer(sorted_list_of_dics)