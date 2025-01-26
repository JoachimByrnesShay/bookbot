
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # numWords = countWords(file_contents)
        # print(numWords)
        # dict = countChars(file_contents)
        # print(dict)
        showReport(file_contents)


def countWords(text):
    return len(text.split())

def countChars(text):
    result = {}
    #alpha = r'[a-z]'

    for c in text:
        if not c.isalpha():
            continue
        current = c.lower() 
        if current in result:
            result[current]+=1
        else:
            result[current]=1
    return result

def showReport(text):
    dict = countChars(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{countWords(text)} words found in the document')
    print("")
    print("testline")
    for char in dict:
        print(f'The \'{char}\' was found {dict[char]} times')

main()