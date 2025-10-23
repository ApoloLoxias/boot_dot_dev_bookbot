##################################
# Counters
##################################

def word_counter(text_string):
    return(len(text_string.split()))

def key_counter(keys):
    dic = {}
    for key in keys: 
        try:
            dic[key] += 1
        except Exception:
            dic[key] =  1
    return dic

##################################
#Sorting
##################################

# Function that turns a dictionary of char: count pairs into a list of dictionarys with {"char": char, "count" count} pairs
# It helps with sorting
def helper_function(dic):
    helper_list = []
    for key in dic:
        helper_list.append({"char": key, "count": dic[key]})
    return helper_list

#Sorting proper

# helper function for .sort()
def sort_on(items):
    return items["count"]

def sort_on_follow_up(list):
    list.sort(reverse = True, key=sort_on)
    return list

# Nested function for reduced insanity check DC on code reading
def sort_dic(dic):
    return sort_on_follow_up(helper_function(dic))

# Like the funcition above, but only for alphabetical characters
def sort_alpha(dic)
    return sort_on_follow_up(helper_function(only_alpha(dic)))

##################################
# Exclusion of non alphabetical characters
##################################

def only_alpha(dic):
    alpha_dic = {}
    for key in dic:
        if key.isalpha():
            alpha_dic[key] = dic [key]
    return alpha_dic