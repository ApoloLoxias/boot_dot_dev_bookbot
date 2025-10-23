# ====================================================================
#-------------------------IMPORTING FUNCTIONS-------------------------
# ====================================================================

from stats import word_counter, key_counter, sort_dic, sort_alpha, sort_nalpha
import sys

# ====================================================================
#--DEFINING FUNCTIONS FOR GETTING BOOK CONTENT AND PRINTING OUTPUTS--
# ====================================================================

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def list_chars(string):
    separator = "super_special_separator_that_is_highly_unlikely_to_naturaly_appear_in_a_given_written_text_'Rq9*c8;tCI9"
    return separator.join(string).split(separator)

def pretty_printer(sorted_list_of_dics):
    for dic in sorted_list_of_dics:
        print(f"{dic["char"]}: {dic["count"]}")

# ====================================================================
#---------------------------MAIN FUNCTIONS----------------------------
# ====================================================================


def main(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    book_text_in_lower_case = get_book_text(path_to_book).lower()
    print("----------- Word Count ----------")
    print(f"Found {word_counter(book_text_in_lower_case)} total words")
    print("--------- Character Count -------")
    pretty_printer(sort_alpha(key_counter(list_chars(book_text_in_lower_case))))
    print("============= END ===============")

def flagged_main(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    book_text_in_lower_case = get_book_text(path_to_book).lower()
    print("----------- Word Count ----------")
    print(f"Found {word_counter(book_text_in_lower_case)} total words")
    print("--------- Character Count -------")
    pretty_printer(sort_nalpha(key_counter(list_chars(book_text_in_lower_case))))
    print("============= END ===============")
# ====================================================================
#----------------------------CODE EXECUTION---------------------------
# ====================================================================

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
try:
    if sys.argv[2] == "--non-alpha": print("non-alpha flag")
    else: print("flag not recognized")
except Exception: pass

# main(sys.argv[1])
flagged_main(sys.argv[1])