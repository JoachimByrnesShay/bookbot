import sys

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = read_file(path_to_file)
    # print(file_contents)
    print(count_words(file_contents))
    print(count_letters(file_contents))
    print_report(path_to_file, file_contents)

def read_file(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_letters(text):
    result = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if result.get(lowered):
                result[lowered] += 1
            else:
                result[lowered] = 1
    return result

def print_report(path_name, text):
    word_count = count_words(text)
    letter_count = count_letters(text)
    sortedItems = sorted(letter_count.items(), key=lambda kv: ((kv[1], kv[0])), reverse=True)

    print(f"--- Begin report of {path_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter, count in sortedItems:
        print(f"the '{letter}' character was found {count} times")
    print("--- End report ---")

if __name__ == '__main__':
    sys.exit(main())