def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    letter_freq = {}
    for ch in text:
        char = ch.lower() 
        if not char in letter_freq:
            letter_freq[char] = 1
        else:
            letter_freq[char]+=1
    return letter_freq

def get_annotated_chars_with_count(dictionary):
    def sort_on(items):
        return items["num"]

    char_list = []
    for key in dictionary:
        char_list.append({"char": key, "num": dictionary[key]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
