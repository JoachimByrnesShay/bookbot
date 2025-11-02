import sys
from stats import get_num_words, get_num_chars, get_annotated_chars_with_count

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() 
    return file_contents

filepath = sys.argv[1]
text = get_book_text(filepath)



message = f"Found {get_num_words(text)} total words"
print(message)

char_dict = get_num_chars(text)

sorted_list = get_annotated_chars_with_count(char_dict)

for stat in sorted_list:
    if stat["char"].isalpha():
        print(stat["char"] + ": " + str(stat["num"]))