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