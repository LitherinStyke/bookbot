def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_words_from_book(path_to_file:str):
    book_contents = get_book_text(path_to_file)
    words = book_contents.split()
    return words

def main():
    print(f'{len(get_words_from_book('books/frankenstein.txt'))} words found in the document')

main()